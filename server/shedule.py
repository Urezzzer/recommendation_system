from app import scheduler

# Планируется задание расписания для преобразования данных, переобучения моделей и получения предсказаний

# @scheduler.task('cron', id='do_job_2', minute='0 0 20 1 *')
# def preprocess_data():
#    print('Data processed!')


# @scheduler.task('cron', id='do_job_2', minute='0 0 23 1 *')
# def fit_models():
#    print('Model fitted!')

# @scheduler.task('cron', id='do_job_2', minute='0 0 23 ? * Monday')
# def get_predictions():
#    print('Predictions got!')
