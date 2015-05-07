
<!DOCTYPE html>
<html lang="ru" xml:lang="ru">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="http://getbootstrap.com/favicon.ico">

    <title>EXPERTISE</title>
	

    <!-- Bootstrap core CSS -->
    <link href="http://www.oneskyapp.com/ru/docs/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="http://www.oneskyapp.com/ru/docs/bootstrap/examples/dashboard/dashboard.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="http://getbootstrap.com/assets/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->


  <meta class="os-tdn" http-equiv="Content-Language" content="ru"><meta class="os-tdn" property="og:locale" content="ru"></head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          
          <a class="navbar-brand" href="#" data-replace-tmp-key="7adea0d9c77aabccd8bb67ae0a832d59"><os-p key="7adea0d9c77aabccd8bb67ae0a832d59">EXPERTISE</os-p></a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
           
            <li><a href="#" data-replace-tmp-key="6a26f548831e6a8c26bfbbd9f6ec61e0"><os-p key="6a26f548831e6a8c26bfbbd9f6ec61e0">About</os-p></a></li>
          </ul>
         
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-4 col-md-4 sidebar">
         <div class="panel panel-primary">
				
			<div class="panel-heading">Темы новостей</div>
			
			<div class="panel-body" id="blockWaiting" style="display:none;">
				<div class="progress progress-striped active">
					<div class="progress-bar"  role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">Подождите, информация загружается...</div>
				</div>
			</div>
				
			<div class="panel-body" id="blockTopics">
			<b><span id="siteTitle">Выберите сайт с новостями</span></b><br>
			<div id="newsLinks">
			
			</div>
				</div>
		</div>
		
		  <div class="panel panel-primary">
				
			<div class="panel-heading">Сайты с новостями</div>
			<div class="panel-body">
			<div class="row newsSites">
			<div class="col-sm-4  col-md-4">
			
        <a href="#" feed="http://news.yandex.ru/auto.rss">Авто</a><br>
		<a href="#" feed="http://news.yandex.ru/computers.rss">Hi-Tech</a><br>
		<a href="#" feed="http://news.yandex.ru/software.rss">Софт</a><br> 
		</div>
		<div class="col-sm-4  col-md-4">
			
		 <a href="#" feed="http://news.yandex.ru/law.rss">Право</a><br>
		 <a href="#" feed="http://news.yandex.ru/incident.rss">Происшествия</a><br>
		 <a href="#" feed="http://news.yandex.ru/fire.rss">Пожары</a><br>
		</div>
		<div class="col-sm-4  col-md-4">
			
         <a href="#" feed="http://news.yandex.ru/business.rss">Экономика</a><br>
		 <a href="#" feed="http://news.yandex.ru/culture.rss">Культура</a><br>
		 <a href="#" feed="http://news.yandex.ru/internet.rss">Интернет</a><br> 
		</div>
		</div>
				</div>
		</div>
          
        </div>
        <div class="col-sm-8 col-sm-offset-4 col-md-8 col-md-offset-4 main">
		
			
             
			 <div id="article">
		  <h2 class="page-header" id="pageTitle">Здесь могла бы быть Ваша реклама!</h2>
		  <div id="details" style="font-size:16pt">
	 </div>
	 
		 <br> 
		 <div id="expertsBlock" style="display:none;" class="text-center">
<form action="#" method="post">
<p><button type="button" id="buttonExpert" class="btn btn-info">Найти эксперта</button></p>
</form>	 
			 </div>
		 	   </div>
			   
			   <div id="listexpert" style="display:none;">
			  <div class="row">
			  <div class="col-sm-8" id="table"><h1 class="page-header" id="pageTitle">Эксперты:</h1>  <p id="searchResult"></p></div>
			  
			    <div class="col-sm-4" id="table"> <table class="table class="table table-hover">

   <strong>Категории: </strong>
 
  <tbody>
    <tr  class="success">
      <td>Право</td>
    </tr>
	 <tr  class="success">
      <td>Экономика</td>
    </tr>
	<tr  class="success">
      <td>Биржа</td>
    </tr>
	 <tr  class="success">
      <td>Разработка</td>
    </tr>
	<tr  class="success">
      <td>Риск менеджмент</td>
    </tr>
	 <tr  class="success">
      <td>Литература</td>
    </tr>
	<tr  class="success">
      <td>Перевод</td>
    </tr>
	 <tr  class="success">
      <td>Независимость</td>
    </tr>
	<tr  class="success">
      <td>Мотивация</td>
    </tr>
	 <tr  class="success">
      <td>Математика</td>
    </tr>
  </tbody>

		</table></div>
				</div>
			   </div>
			  
		   
		   
		</div>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
<style type="text/css">
    h3 { margin-bottom: 5px; }
    div.updated { color: #999; margin-bottom: 5px; font-size: 0.8em; }
</style>
<script type="text/javascript" src="js/jquery.js"></script>
<script type="text/javascript" src="js/jquery.jfeed.pack.js"></script>


<script type="text/javascript">

jQuery(function() {
	$(".newsSites a").click(function(){
	var link=$(this).attr("feed");
		
$("#blockTopics").slideUp();
$("#blockWaiting").slideDown();
    jQuery.getFeed({
        url: 'proxy.php?url='+link,
        success: function(feed) {
			$("#blockWaiting").slideUp();
			$("#blockTopics").slideDown();
			$("#listexpert").hide();
			$("#table").hide();
			$("#siteTitle").text(feed.title);
			$("#pageTitle").show();
			
            
			 
			
            var html = '';
            anons = new Array();
			
            for(var i = 1; i < feed.items.length && i <= 5; i++) {
            
                var item = feed.items[i];
                
                html += '<h5>'
                + '<a class="anonsLink" href="#" newsId="'
                + i
                + '">'
                + item.title
                + '</a>'
                + '</h5>';
                
				anons[i] = {};
				anons[i].title = item.title;
				anons[i].description = item.description;
            }
            
            jQuery('#newsLinks').html(html);
        },
		error: function(jqXHR, textStatus) {
			$("#blockWaiting").slideUp();
			$("#blockTopics").slideDown();
			$("#siteTitle").text("Error!");
			$("#newsLinks").text(textStatus);
		}
    });
	
	return false;
	});
	
	$(".anonsLink").live('click', function(){
		var anonsId=$(this).attr("newsId");
		$("#pageTitle").html(anons[anonsId].title);
		$("#details").html(anons[anonsId].description);
		$("#expertsBlock").show();
		$("#listexpert").hide();
		$("#table").hide();
		$("#article").show();
		
		return false;
	});
	

	$("#buttonExpert").click(function() {
  $.ajax({
  type: 'POST',
  url: '/cgi-glob/parser.py',
  data: 'json',
  dataType: 'json',
 
success: function(res){
  jQuery.each(res, function(id, person) {
      $("#searchResult").append("<table class='table'><tbody><tr class='success'><td><img src="+person.photo+" width='110' height='140' align='left' alt=''><p><h4 align='center'><a href="+id+" >"+person.fio+"</a></h4><p align='center'>"+person.academic_title1+", "+person.academic_title+" </p></td></tr></tbody></table><br>");
      
	});
	$("#article").hide();
	$("#listexpert").show();
	$("#table").show();

	
  },
  error: function(){
    alert("ERR");
  }


	});
});
	
});


</script>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-55658713-1', 'auto');
  ga('send', 'pageview');

</script>
<!--("+person.pos+")("+person.academic_title+")ДЛЯ ДОЛДНОСТИ!!!> 
</body>
</html>