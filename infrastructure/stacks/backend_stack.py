from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigw,
    Duration,
)
from constructs import Construct

class BackendStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda function
        api_lambda = lambda_.Function(
            self,
            "ApiFunction",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="main.handler",
            code=lambda_.Code.from_asset("../backend"),
            timeout=Duration.seconds(30),
        )

        # API Gateway
        api = apigw.LambdaRestApi(
            self,
            "ApiGateway",
            handler=api_lambda,
            proxy=True,
        )
