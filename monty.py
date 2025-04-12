import random

def monty_hall_simulation(switch: bool, trials: int = 1000) -> float:
    wins = 0

    for _ in range(trials):

        doors = [0, 1, 2]
        car = random.choice(doors)

        choice = random.choice(doors)
        
        remaining_doors = [d for d in doors if d != choice and d != car]
        host_opens = random.choice(remaining_doors)

        if switch:
            choice = next(d for d in doors if d != choice and d != host_opens)

    
        if choice == car:
            wins += 1

    win_rate = wins / trials
    return win_rate

print("Win rate when staying:", monty_hall_simulation(switch=False))
print("Win rate when switching:", monty_hall_simulation(switch=True))
