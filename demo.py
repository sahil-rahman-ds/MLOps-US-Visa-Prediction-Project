
# import os
# from US_Visa.constants import MONGODB_URL_KEY
# mongodb_url = os.getenv(MONGODB_URL_KEY)
# print(mongodb_url)

from US_Visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()