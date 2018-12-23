% include('header.tpl', tags=tags)

<div id="content" class="mui-container-fluid">

	<div class="mui-row">
		<div class="mui-col-sm-10 mui-col-sm-offset-1">

			<div class="mui--text-dark-secondary mui--text-body1">
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
				<h1>
					Daily Big Data Tips [{{ len(tips) }}]
					% if search_tag:
						<small>&nbsp;(<a href="/">show all</a>)</small>
					% end
				</h1>
			</div>
			<div class="mui-divider"></div>
			% for tip in tips:
				<div class='tip'>
					<pre>{{ !tip.text }}</pre>
					<div class="mui--z4 mui-panel mui--text-danger">
						<strong>{{ tip.likes }}</strong>&ensp;<i class="fa fa-heart"></i>&emsp;|&emsp;
						<strong>{{ tip.retweets }}</strong>&ensp;<i class="fa fa-twitter"></i>&emsp;|&emsp;
						<strong class="mui--text-dark-hint">{{ tip.created }}</strong>&ensp;<i class="fa fa-calendar"></i>&emsp;|&emsp;
						<a href="https://twitter.com/bigdata_tip/status/{{ tip.tweetid }}" target="_blank"><i class="fa fa-share-alt"></i></a>
					</div>
				</div>
			% end

		</div>
	</div>

</div>

% include('footer.tpl')
