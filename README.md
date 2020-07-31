# Domain tcping

检测阿里云配置 dns 解析中的域名，已经开启80端口，但是未开启443端口的域名 

### 环境：  
```
python >= v3.6  
pip >= v20.2 
``` 
 
### 安装依赖:
```bash
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

### 发送通知给多个人:  
- 在企业微信后台添加应用可见范围
- 修改config.json
```json
{
  "ToUser": "user1|user2"
}
```

### 构建
```bash
sh build.sh
```

### 运行  
```bash
docker run -it --rm reg.nexus.wmqhealth.com/tools/domain-ping:v1
```
