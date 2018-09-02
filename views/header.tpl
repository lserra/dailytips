<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="//cdn.muicss.com/mui-0.9.28/css/mui.min.css" rel="stylesheet" type="text/css" />
	<!-- load icon font -->
    <link href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet" type="text/css" />
    <!-- load MUI -->
    <link href="static/css/style.css" rel="stylesheet" type="text/css" />
    <script src="//cdn.muicss.com/mui-0.9.28/js/mui.min.js"></script>
    <title>datafesh tips</title>
  </head>
  <body>

  <div id="sidebar">

    <div class="mui--text-light mui--text-headline">
      <a href="/" target="_blank">
        <img class="mui--align-middle" src='static/img/bigdata.png' alt='Daily Big Data Tips' height="100%" width="100%">
      </a>
      <!--<a href="https://pybit.es" target="_blank">-->
        <!--<img class="logo" src='https://pybit.es/images/pybites.png' alt='PyBites'>-->
      <!--</a>-->
    </div>

	<form action="/" method="GET" class="mui-form--inline">
		<div class="mui-textfield">
			<input type="text" name="tag" placeholder="Search" value="{{ search_tag }}">
		</div>
		<button class="mui-btn" disabled><i class="fa fa-search"></i></button>
	</form>

	% for tag in tags:
	  <a style="font-size: {{ tag.count/10 + 1 }}em;" href="/{{ tag.name }}">#{{ tag.name }}</a>&nbsp;&nbsp;
	% end
	<br>
	<br>
	<a href="https://goo.gl/forms/qYMXKTVGrD4dM3Aq2" target="_blank">
		<button class="mui-btn mui-btn--small mui-btn--primary mui-btn--raised">New Tip</button>
	</a>
	<div class="mui-dropdown">
	<button class="mui-btn mui-btn--small mui-btn--primary mui-btn--raised" data-mui-toggle="dropdown">
		More Tips
		<span class="mui-caret"></span>
	</button>
	<ul class="mui-dropdown__menu">
		<li><a href="https://medium.com/" target="_blank">Medium</a></li>
		<li><a href="http://binapratica.blogspot.com/" target="_blank">Blogger</a></li>
		<li><a href="http://lserra.datafresh.com.br/" target="_blank">datafresh</a></li>
		<li><a href="http://www.datafresh.com.br/" target="_blank">dash.io</a></li>
	</ul>
	</div>
  </div>
