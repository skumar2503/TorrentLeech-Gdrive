from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1424392005:AAF1lbyIA-lkUUoagwwxAA-JIu9roo-AZtY"
    APP_ID = 1368264
    API_HASH = "e71fe0dcd8585c41201187161a42b904"
    OWNER_ID = 530361591
    AUTH_CHANNEL = [-1001203524916]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMDPN9DLBlUAAMGXAmvLM7RSOAOjrJ9TDaSLHtL1sDQCUaeFSVmz5JUnSo_ysSCP9WFIL5q-Mv1KdoRAXP5ktxoj2AlNBWq2D8NksPlOblsMiR1aRHKuJD1oG1o6o_y992HaF27jSO8mS1SloL9devmxoVLZtYgu0JKU0JA","token_type":"Bearer","refresh_token":"1//05rLbGQqWwYHZCgYIARAAGAUSNwF-L9IrnPbr6ndpobe45gDA9eMOS9DMz0EqrLg2rtC-1p9iHTpZVsxZptkAuR44aT7SRYt3alo","expiry":"2020-11-28T13:09:34.622785719Z"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
