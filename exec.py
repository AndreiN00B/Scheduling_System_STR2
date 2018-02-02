from Schedule_Generator import schedule

sched = schedule()
liss = ["Math" * 3, "Filipino" * 3, "English" * 3, "Computer Science" * 5, "Physics" * 5]
sched.gen_schedule(liss)
sched.output_schedule()
