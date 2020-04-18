#!/bin/sh
# Create project tree
sh ./scripts/make_tree.sh

# Copy static assets
sh ./scripts/copy_static.sh

# Export index and pages
sh ./scripts/export_index.sh
sh ./scripts/export_pages.sh

# Export posts
sh ./scripts/export_posts.sh

# Export talks
sh ./scripts/export_talks.sh
