const app = new Vue({
    el: '#app',
    data() {
        return {
            contents:[],//所有评论信息
            baseURL:'http://127.0.0.1:8000/',//获取后端的启动接口
            input:{
                content:'',
                name:'',
            },
        }
    },
    mounted() {
        //自动加载数据
        this.getContents();
    },
    methods:{
        //获取数据库所有的信息
        getContents:function(){
            //
            let that=this
            //是有axios实现Ajax请求
            axios
            .get(that.baseURL+"contents/")
            .then(function(res){
                //请求成功后返回执行函数
                 if (res.data.code==1){
                     //吧获取的数据给contents
                     that.contents=res.data.data;
                     //提示消息框
                     that.$message({
                         message: '操作成功',
                         type:'success'
                     });
                 }else{
                     //失败提示
                     that.$message.console.error(res.data.msg)
                 }
            })
            .catch(function(error){
                console.log(error);
                that.$message.error("获取后端查询异常")
            });
        },
        //添加评论到数据库
        Addcontent(){
            //定义that
            let that=this
            //执行axios请求
            axios.post(that.baseURL+'add_contents/',that.input)
                .then(res=>{
                    //执行成功
                    if (res.data.code==1){
                        //获取所有评论信息
                        that.contents=res.data.data;
                        //提示
                        that.$message({
                            message: '操作成功',
                            type:'success'
                        });
                    }else{
                        //失败提示
                        that.$message.console.error(res.data.msg)
                    }
                })
                .catch(function(error){
                    //执行失败
                    console.log(error);
                    that.$message.error("获取后端查询异常")
                });
        }
    },
})