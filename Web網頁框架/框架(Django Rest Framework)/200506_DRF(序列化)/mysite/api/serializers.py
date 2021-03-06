from rest_framework import serializers
from api import models


class RolesSerializer(serializers.Serializer):
    # 字段名必須跟數據庫一致，除非有加source參數
    id = serializers.IntegerField()
    title = serializers.CharField()

# 方法一：
# class UsersSerializer(serializers.Serializer):
#     # 字段名必須跟數據庫一致，除非有加source參數
#     # 一般字段
#     id = serializers.IntegerField()
#     username = serializers.CharField()
#     password = serializers.CharField()
#     # choices字段
#     user_type_num = serializers.CharField(source='user_type')  # source表示要去哪個字段
#     # get_字段名_display： 他會先取出字段名對應的數據，但如果是可被執行的話，就會繼續找下去
#     user_type = serializers.CharField(source='get_user_type_display')  # 取出來的是VIP、SIP等
#     # 一對多字段
#     groups = serializers.CharField(source='group.title')  # 取出外鍵對象.title字段
#     # 多對多字段
#     rls = serializers.SerializerMethodField()  # 自定義顯示
#
#     def get_rls(self, obj):  # 自定義顯示的方法，名稱為get_字段名
#         roles_obj_list = obj.roles.all()
#         ret = []
#         for item in roles_obj_list:
#             ret.append({'id': item.id, 'title': item.title})
#         return ret  # 要顯示的數據


# 方法二(優)：
# class UsersSerializer(serializers.ModelSerializer):
#     # choices字段
#     # get_字段名_display： 他會先取出字段名對應的數據，但如果是可被執行的話，就會繼續找下去
#     type = serializers.CharField(source='get_user_type_display')  # 取出來的是VIP、SIP等
#     # 一對多字段
#     groups = serializers.CharField(source='group.title')
#     # 多對多字段
#     rls = serializers.SerializerMethodField()  # 自定義顯示
#
#     def get_rls(self, obj):  # 自定義顯示的方法，名稱為get_字段名
#         roles_obj_list = obj.roles.all()
#         ret = []
#         for item in roles_obj_list:
#             ret.append({'id': item.id, 'title': item.title})
#         return ret  # 要顯示的數據
#
#     class Meta:
#         model = models.UserInfo  # 關聯的表
#         # fields = '__all__'
#         # 只能用於簡單的字段
#         fields = ['id', 'username', 'password', 'type', 'groups', 'rls']  # 要顯示的字段


# 方法三(推薦)：
# class UsersSerializer(serializers.ModelSerializer):
#     type = serializers.CharField(source='get_user_type_display')
#
#     class Meta:
#         model = models.UserInfo  # 關聯的表
#         fields = ['id', 'username', 'password', 'type', 'group', 'roles']
#         # 透過設置深度可以很輕鬆的獲取關聯表的所有數據。(建議範圍1~10)
#         # 但無法取到choices字段
#         depth = 1  # 深度，若不想要關聯表詳細數據可以設為0


# 方法四(透過生成鏈結進行深度查詢)：
class UsersSerializer(serializers.ModelSerializer):
    # lookup_field為要去深度查的外鍵字段
    # lookup_url_kwarg為url中我們設置的變量名
    # view_name為url的別名
    gp_url = serializers.HyperlinkedIdentityField(
        lookup_field='group_id', lookup_url_kwarg='fk', view_name='gp')

    class Meta:
        model = models.UserInfo  # 關聯的表
        fields = ['id', 'username', 'password', 'gp_url']


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserGroup  # 關聯的表
        fields = '__all__'
