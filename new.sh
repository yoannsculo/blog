#!/bin/bash

POSTS="./_posts"

if [ ! -d $POSTS ]; then
	echo "_posts directory not found !"
	exit -1
fi

DATE=`date +%Y-%m-%d-%H-%M`
FILE="$POSTS/$DATE-new_article.markdown2"

touch $FILE

cat > $FILE << "EOF"
---
layout: post
title: 
keywords:
publish: false
---
EOF

