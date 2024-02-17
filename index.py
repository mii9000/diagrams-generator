from diagrams import Diagram, Cluster
from diagrams.aws.database import RDS, Redshift
from diagrams.aws.analytics import Glue
from diagrams.aws.storage import S3

with Diagram("", show=False, direction="TB", filename="output/diagram", outformat="png"):
    with Cluster("Source"):
        postgres = RDS("PostgreSQL")

    with Cluster("AWS Glue"):
        glue_etl = Glue("ETL Job")

    with Cluster("Storage"):
        s3_bucket = S3("S3 Bucket")

    with Cluster("Target"):
        redshift = Redshift("RedShift")

    postgres >> glue_etl >> s3_bucket >> redshift
