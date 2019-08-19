#每次都要用到查询的视图


from goods.models import GoodsChannel




def get_categories():

    # 查询所有的频道
    channel_list = GoodsChannel.objects.order_by('group_id').order_by("sequence")
    # 构造结果字典

    categories = {}
    # 遍历频道，添加分类信息
    for channel in channel_list:
        # 判断频道是否已经存在
        if channel.group_id not in categories:
            # 不存在则新建频道
            categories[channel.group_id] = {
                'channels': [],
                'sub_cats': []
            }
        # 获取某个频道的数据
        '''
        {
                'channels': [{'url':'http://shouji.jd.com','name':'手机'}],
                'sub_cats': [....]
            }
        '''
        # channel_dict=categories[channel.group_id]
        # 添加一级分类
        '''
        {
                'channels': [
                    {'url':'http://shouji.jd.com','name':'手机'}
                ],
                'sub_cats': []
            }
        '''
        categories[channel.group_id]['channels'].append({'url': channel.url, 'name': channel.category.name})
        # 添加二级分类
        for sub2 in channel.category.subs.all():
            # 添加三级分类
            sub2.sub_cats = sub2.subs.all()  # [category,catetory,...]
            # 将二级分类添加到列表中
            categories[channel.group_id]['sub_cats'].append(sub2)
    return categories