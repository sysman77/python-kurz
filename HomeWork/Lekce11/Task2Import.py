import random
import statistics

class BoatLanding:
    def __init__(self, avg_interarrival_time, avg_disembark_time, max_people):
        self.avg_interarrival_time = avg_interarrival_time
        self.avg_disembark_time = avg_disembark_time
        self.max_people = max_people
        self.current_time = 0
        self.people_on_dock = []
        self.disembark_times = []
        self.queue = []

    def run(self, sim_time):
        while self.current_time < sim_time:
            # Generate next boat arrival time
            next_arrival = self.current_time + random.expovariate(1.0 / self.avg_interarrival_time)
            if next_arrival >= sim_time:
                break

            self.current_time = next_arrival
            print(f'Boat arrived at {self.current_time}')

            num_passengers = random.randint(1, 50)  # Random number of passengers
            for _ in range(num_passengers):
                if len(self.queue) < self.max_people:
                    self.queue.append(self.current_time)

            self.disembark_passengers()

        self.finish_disembark()

    def disembark_passengers(self):
        while self.queue and len(self.people_on_dock) < self.max_people:
            arrival_time = self.queue.pop(0)
            disembark_time = random.expovariate(1.0 / self.avg_disembark_time)
            self.people_on_dock.append((arrival_time, self.current_time + disembark_time))
            print(f'Person disembarked at {self.current_time + disembark_time}, arrived at {arrival_time}')

    def finish_disembark(self):
        for arrival_time, finish_time in self.people_on_dock:
            self.disembark_times.append(finish_time - arrival_time)
        self.people_on_dock = []

def run_simulation(avg_interarrival_time, avg_disembark_time, max_people, sim_time):
    boat_landing = BoatLanding(avg_interarrival_time, avg_disembark_time, max_people)
    boat_landing.run(sim_time)
    return boat_landing

# Parameters
avg_interarrival_time = 30  # Average time between boat arrivals in minutes
avg_disembark_time = 1  # Average time for a passenger to disembark in minutes
max_people = 10  # Max people allowed on the dock at one time
sim_time = 8 * 60  # Simulation time in minutes (e.g., 8 hours)

# Run simulation
boat_landing = run_simulation(avg_interarrival_time, avg_disembark_time, max_people, sim_time)

# Results
if boat_landing.disembark_times:
    print(f'Average time on dock: {statistics.mean(boat_landing.disembark_times)} minutes')
    print(f'Number of disembarked passengers: {len(boat_landing.disembark_times)}')
else:
    print('No passengers disembarked.')
