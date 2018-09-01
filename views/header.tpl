<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="//cdn.muicss.com/mui-0.9.28/css/mui.min.css" rel="stylesheet" type="text/css" />
    <link href="static/css/style.css" rel="stylesheet" type="text/css" />
    <script src="//cdn.muicss.com/mui-0.9.28/js/mui.min.js"></script>
    <title>Daily Python Tip</title>
  </head>
  <body>

  <div id="sidebar">

    <div class="mui--text-light mui--text-display1 mui--align-vertical">
      <a href="https://twitter.com/python_tip" target="_blank">
        <img class="logo" src='https://pbs.twimg.com/profile_images/828169453095510016/X0iDPdDL_400x400.jpg' alt='PyBites'>
      </a>
      <a href="https://pybit.es" target="_blank">
        <img class="logo" src='https://pybit.es/images/pybites.png' alt='PyBites'>
      </a>
    </div>

	<form action="/" method="GET" class="mui-form">
		<div class="mui-textfield">
			<input type="text" name="tag" placeholder="Search" value="{{ search_tag }}">
		</div>
	</form>

	% for tag in tags:
	  <a style="font-size: {{ tag.count/10 + 1 }}em;" href="/{{ tag.name }}">#{{ tag.name }}</a>&nbsp;&nbsp;
	% end
	<br>
	<br>
	<a href="https://docs.google.com/forms/d/e/1FAIpQLScsHklRH2-uplGYH_vxhtIin-zJS44bXQkAWCH7_N7nUdrGXw/viewform" target="_blank">
		<button class="mui-btn mui-btn--primary">New Tip</button>
	</a>
	<div class="mui-dropdown">
	<button class="mui-btn mui-btn--primary" data-mui-toggle="dropdown">
		About
		<span class="mui-caret"></span>
	</button>
	<ul class="mui-dropdown__menu">
		<li><a href="https://twitter.com/bbelderbos" target="_blank">Created by @bbelderbos (@pybites)</a></li>
		<li><a href="https://pybit.es/codechallenge40.html" target="_blank">Built for PyBites Challenge #40</a></li>
		<li><a href="https://github.com/pybites/pytip" target="_blank">Star / fork the Github repo</a></li>
	</ul>
	</div>

  </div>
