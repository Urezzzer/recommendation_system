from app import scheduler

# if you have separate task, and you don't want to run it every 5 seconds
# you can use interval argument in decorator
# @scheduler.task('interval', id='do_job_1', seconds=1, misfire_grace_time=900)
# def job1():
#    print('Job 1 executed')

# cron examples
# @scheduler.task('cron', id='do_job_2', minute='*')
# def job2():
#    print('Job 2 executed')
