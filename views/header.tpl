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
    <title>datafresh</title>
		<link rel="apple-touch-icon" sizes="180x180" href="/static/img/apple-touch-icon.png">
		<link rel="icon" type="image/png" sizes="32x32" href="/static/img/favicon.ico">
		<link rel="icon" type="image/png" sizes="32x32" href="/static/img/favicon-32x32.png">
		<link rel="icon" type="image/png" sizes="16x16" href="/static/img/favicon-16x16.png">
		<link rel="manifest" href="/static/site.webmanifest">
		<link rel="mask-icon" href="/static/img/safari-pinned-tab.svg" color="#5bbad5">
		<meta name="msapplication-TileColor" content="#da532c">
		<meta name="theme-color" content="#ffffff">		
  </head>
  <body>

  <div id="sidebar">

    <div class="mui--text-light mui--text-headline">
      <a href="/" target="_blank">
        <img class="mui--align-middle" src='static/img/bigdata.png' alt='Daily Big Data Tips' height="85%" width="85%">
      </a>
    </div>

	<form action="/" method="GET" class="mui-form--inline">
		<div class="mui-textfield">
			<input type="text" name="tag" placeholder="Search" value="{{ search_tag }}">
		</div>
		<button class="mui-btn" disabled><i class="fa fa-search"></i></button>
	</form>
	% for tag in tags:
	  <a href="/{{ tag.name }}">#{{ tag.name }}</a>&nbsp;&nbsp;
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
      <li><a href="http://www.datafresh.com.br/" target="_blank">datafresh</a></li>
      <li><a href="http://www.datafresh.com.br/helloworld/" target="_blank">github</a></li>
      <li><a href="http://binapratica.blogspot.com/" target="_blank">blog</a></li>
      <li><a href="https://medium.com/" target="_blank">medium</a></li>
    </ul>
  </div>
  </div>
