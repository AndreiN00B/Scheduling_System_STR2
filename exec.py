from Schedule_Generator import schedule

sched = schedule()
liss = ["Math", "Filipino", "English", "Computer Science", "Physics"] * 5
sched.gen_schedule(liss)
sched.output_schedule()
