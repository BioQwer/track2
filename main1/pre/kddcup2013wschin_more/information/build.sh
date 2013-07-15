#!/bin/sh
perl filter.pl TW.raw More.raw > last.less
perl filter.pl CN.raw KR.raw TW.raw More.raw > last.more
perl filter.pl Chinese.token More.token > token.all
