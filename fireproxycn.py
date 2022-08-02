# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import argparse
from typing import Tuple

from alibabacloud_cloudapi20160714.client import Client as CloudAPI20160714Client
from alibabacloud_cloudapi20160714.models import DescribeRegionsResponse, DescribeApiGroupsResponse
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cloudapi20160714 import models as cloud_api20160714_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:

    def __init__(self, accessKeyId, accessKeySecret, endpoint="apigateway.cn-hangzhou.aliyuncs.com"):
        self.accessKeyId = accessKeyId
        self.accessKeySecret = accessKeySecret
        self.endpoint = endpoint
        self.client = self.create_client()
        # self.regions = self.getRegions(accessKeyId, accessKeySecret)

    def create_client(self) -> CloudAPI20160714Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的 AccessKey ID,
            access_key_id=self.accessKeyId,
            # 您的 AccessKey Secret,
            access_key_secret=self.accessKeySecret
        )
        # 访问的域名
        config.endpoint = self.endpoint
        return CloudAPI20160714Client(config)

    def getRegions(self) -> DescribeRegionsResponse:
        describe_regions_request = cloud_api20160714_models.DescribeRegionsRequest()
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.describe_regions_with_options(describe_regions_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def getGroups(self) -> DescribeApiGroupsResponse:
        describe_api_groups_request = cloud_api20160714_models.DescribeApiGroupsRequest()
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.describe_api_groups_with_options(describe_api_groups_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def getDeployedApiList(self):
        describe_deployed_apis_request = cloud_api20160714_models.DescribeDeployedApisRequest()
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.describe_deployed_apis_with_options(describe_deployed_apis_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def getDescribeApi(self, group_id):
        describe_apis_request = cloud_api20160714_models.DescribeApisRequest(
            group_id=group_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.describe_apis_with_options(describe_apis_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def setGroup(self, groupName="fireproxycn"):
        create_api_group_request = cloud_api20160714_models.CreateApiGroupRequest(
            group_name=groupName,
            base_path='/',
            description=groupName + ' group'
        )
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.create_api_group_with_options(create_api_group_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def deleteGroup(self, group_id):
        delete_api_group_request = cloud_api20160714_models.DeleteApiGroupRequest(
            group_id=group_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.delete_api_group_with_options(delete_api_group_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def setApiGateway(self, group_id, url):
        create_api_request = cloud_api20160714_models.CreateApiRequest(
            visibility='PRIVATE',
            api_name='fireproxycn',  # todo
            description='fireproxycn api',
            request_config="{\"RequestProtocol\":\"HTTP,HTTPS\",\"RequestHttpMethod\":\"ANY\",\"RequestPath\":\"/*\","
                           "\"BodyFormat\":\"\",\"PostBodyDescription\":\"\",\"RequestMode\":\"PASSTHROUGH\","
                           "\"BodyModel\":\"\"}",
            service_config="{\"ServiceProtocol\":\"HTTP\",\"ServiceHttpMethod\":\"ANY\",\"ServiceAddress\":\"%s\","
                           "\"ServiceTimeout\":\"10000\",\"ServicePath\":\"/*\",\"Mock\":\"FALSE\","
                           "\"MockResult\":\"\",\"OssConfig\":{\"Action\":\"GetObject\"},"
                           "\"ServiceVpcEnable\":\"FALSE\",\"VpcConfig\":{},\"FunctionComputeConfig\":{"
                           "\"FcType\":\"FCEvent\",\"FcRegionId\":\"cn-hangzhou\",\"Path\":\"\",\"FcBaseUrl\":\"\"},"
                           "\"EventBridgeConfig\":{},\"ContentTypeCatagory\":\"CLIENT\",\"ContentTypeValue\":\"\"}" %
                           url,
            group_id=group_id,
            result_type='PASSTHROUGH',
            auth_type="ANONYMOUS",
            backend_enable=False
        )
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.create_api_with_options(create_api_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def deployApi(self, group_id, api_id):
        deploy_api_request = cloud_api20160714_models.DeployApiRequest(
            group_id=group_id,
            api_id=api_id,
            stage_name='RELEASE',
            description='fireproxycn'
        )
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.deploy_api_with_options(deploy_api_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def abolishApi(self, group_id, api_id):
        abolish_api_request = cloud_api20160714_models.AbolishApiRequest(
            group_id=group_id,
            api_id=api_id,
            stage_name='RELEASE'
        )
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.abolish_api_with_options(abolish_api_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def deleteApi(self, group_id, api_id):
        self.abolishApi(group_id, api_id)
        delete_api_request = cloud_api20160714_models.DeleteApiRequest(
            group_id=group_id,
            api_id=api_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.delete_api_with_options(delete_api_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def getApiInfo(self, group_id, api_id):
        describe_api_market_attributes_request = cloud_api20160714_models.DescribeApiMarketAttributesRequest(
            group_id=group_id,
            api_id=api_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.describe_api_market_attributes_with_options(describe_api_market_attributes_request,
                                                                           runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def getApiGroupDescribe(self, group_id):
        describe_api_group_request = cloud_api20160714_models.DescribeApiGroupRequest(
            group_id=group_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            return self.client.describe_api_group_with_options(describe_api_group_request, runtime)
        except Exception as error:
            print(error)
            UtilClient.assert_as_string(error.message)

    def getGroupId(self, groupName):
        gid = None
        groups = self.getGroups()
        if groups.body.total_count != 0:
            for group in groups.body.api_group_attributes.api_group_attribute:
                if group.group_name == groupName:
                    gid = group.group_id
                    break
        return gid

    def createSubdomain(self, groupName, url):
        gid = self.getGroupId(groupName)
        if gid is None:
            gid = self.setGroup(groupName).body.group_id
        api_id = self.setApiGateway(gid, url).body.api_id
        self.deployApi(gid, api_id)
        group_describe = self.getApiGroupDescribe(gid).body
        return group_describe.sub_domain


def getApiGatewayRegions(accessKeyId, accessKeySecret):
    return Sample(accessKeyId, accessKeySecret).getRegions().body.regions.to_map()["Region"]


def listAPI(accessKeyId, accessKeySecret):
    regions = getApiGatewayRegions(accessKeyId, accessKeySecret)
    for region in regions:
        sample = Sample(accessKeyId, accessKeySecret, region["RegionEndpoint"])
        groups = sample.getGroups()
        print(
            f'Region: {region["LocalName"]} Endpoint: {region["RegionEndpoint"]}, Groups TotalCount: {groups.body.total_count}')
        if groups.body.total_count != 0:
            for api_group_attribute in groups.body.api_group_attributes.api_group_attribute:
                group_id = api_group_attribute.group_id
                print(
                    f"\t Group: name: {api_group_attribute.group_name}, id: {group_id}, subDomain: {api_group_attribute.sub_domain}, create time: {api_group_attribute.created_time}")
                if api_group_attribute.group_name == groupName:
                    api_list = sample.getDescribeApi(group_id).body
                    if api_list.total_count != 0:
                        for api in api_list.api_summarys.api_summary:
                            print(f"\t\tAPI: name: {api.api_name}, id: {api.api_id}, create time: {api.created_time}")


def parse_arguments() -> Tuple[argparse.Namespace, str]:
    """Parse command line arguments and return namespace
    :return: Namespace for arguments and help text as a tuple
    """
    parser = argparse.ArgumentParser(description='FireProx API Gateway Manager')
    # parser.add_argument('--profile_name',
    #                     help='AWS Profile Name to store/retrieve credentials', type=str, default=None)
    parser.add_argument('--ak',
                        help='accessKeyId', type=str, default=None)
    parser.add_argument('--aks',
                        help='accessKeySecret', type=str, default=None)
    parser.add_argument('--command',
                        help='Commands: list, create, delete', type=str, default=None)
    parser.add_argument('--endpoint',
                        help='aliyun endpoint (RegionId)', type=str, default=None)
    parser.add_argument('--group_id',
                        help='GROUP ID', type=str, required=False)
    parser.add_argument('--api_id',
                        help='API ID', type=str, required=False)
    parser.add_argument('--all',
                        help='delete all api_id', action='store_true', default=False)
    parser.add_argument('--url',
                        help='target url', type=str, required=False)
    return parser.parse_args(), parser.format_help()


if __name__ == '__main__':

    groupName = "fireproxycn"
    accessKeyId = ""
    accessKeySecret = ""

    args, help_text = parse_arguments()
    if args.command == 'list':
        print(f'Listing API\'s...')
        listAPI(accessKeyId, accessKeySecret)

    elif args.command == 'delete':
        if args.all:
            regions = getApiGatewayRegions(accessKeyId, accessKeySecret)
            for region in regions:
                sample = Sample(accessKeyId, accessKeySecret, region["RegionEndpoint"])
                gid = sample.getGroupId(groupName)
                if gid is not None:
                    api_list = sample.getDescribeApi(gid).body
                    if api_list.total_count != 0:
                        for api in api_list.api_summarys.api_summary:
                            sample.deleteApi(gid, api.api_id)
                            sample.deleteGroup(gid)
                            print(
                                f"Delete Api id: {api.api_id}, Region: {api.region_id}, Group name:  {api.group_name}")

        else:
            sample = Sample(accessKeyId, accessKeySecret, endpoint=args.endpoint)
            sample.deleteApi(group_id=args.group_id, api_id=args.api_id)
            sample.deleteGroup(args.group_id)
            # print(f"Deleting => success")

    elif args.command == 'create':
        if args.endpoint:
            sample = Sample(accessKeyId, accessKeySecret, args.endpoint)
            subdomain = sample.createSubdomain(groupName, args.url)
            print(f"{subdomain} ==> {args.url}")
        else:
            # subdomains = []
            haproxy_backend = ""
            for region in getApiGatewayRegions(accessKeyId, accessKeySecret):
                region_endpoint = region["RegionEndpoint"]
                if 'apigateway.cn' in region_endpoint:
                    # 'apigateway.ap' in region_endpoint:
                    sample = Sample(accessKeyId, accessKeySecret, region_endpoint)
                    subdomain = sample.createSubdomain(groupName, args.url)
                    print(f"{subdomain} {region['LocalName']} Created")
                    haproxy_backend += f"server {subdomain} {subdomain}:80 # {region['LocalName']}\n  "
                    # subdomains.append(
                    #     {"endpoint": region_endpoint, "group_id": group_id, "api_id": api_id, "subdomain": subdomain})
            print(f"""
###################################################
http://127.0.0.1:18000/* ==> {args.url}*
You need to copy the following content to a FILE, run:
haproxy -f FILE
FFUF -w dicc.txt -u http://127.0.0.1:18000/FUZZ
###################################################""")
            haproxy_cfg = """
defaults
  mode http
  timeout client 10s
  timeout connect 5s
  timeout server 10s 
  timeout http-request 10s
  
frontend myfrontend
  bind 127.0.0.1:18000
  default_backend fireproxycn

backend fireproxycn
  http-send-name-header Host
  http-response del-header content-disposition
  %s""" % haproxy_backend
            print(haproxy_cfg)

    else:
        print(help_text)

