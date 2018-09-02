% include('header.tpl', tags=tags)

<div id="content" class="mui-container-fluid">

	<div class="mui-row">
		<div class="mui-col-sm-10 mui-col-sm-offset-1">

			<div class="mui--text-dark-secondary mui--text-body1">
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
					<div class="mui--z4 mui-panel mui--text-danger"><strong>{{ tip.likes }}</strong> Likes | <strong>{{ tip.retweets }}</strong> Retweets | <strong class="mui--text-dark-hint">{{ tip.created }}</strong>  | <a href="https://twitter.com/bigdata_tip/status/{{ tip.tweetid }}" target="_blank"><i class="fa fa-share-alt"></i></a></div>
				</div>
			% end

		</div>
	</div>

</div>

% include('footer.tpl')
