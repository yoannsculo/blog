#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim:syntax=python:sw=4:ts=4:expandtab

# 1 = local
# 0 = remote

site=1

if not site:
        Site.CONTEXT.blog = AttrDict(
                url = 'http://www.yoannsculo.fr',
                images = 'http://www.yoannsculo.fr/images',
                title = 'Yoann Sculo - Ingénieur Linux Embarqué',
                description = 'Yoann Sculo - Blog d\'un Ingénieur Linux Embarqué accro à vim. Bidouille, bricolage, hacking, systèmes embarqués, livres et calembours.',
                language = 'fr',
                author = 'Yoann Sculo',
                mailto = 'yoann.sculo@gmail.com',
                github_growl = 'https://github.com/yoannsculo/growl',
                projects_dir = 'projets',
                keywords = 'yoann, sculo, cv, ingénieur systèmes embarqués, ingénieur, systèmes embarqués, blog,  linux, robotique, utt, UTT, linux embarqué, ARM, embarqué, cross-compilation',
        )
else:
        Site.CONTEXT.blog = AttrDict(
                url = 'http://localhost/blog',
                images = 'http://localhost/blog/images',
                title = 'Yoann Sculo - Ingénieur Linux Embarqué',
                description = 'Yoann Sculo - Blog d\'un Ingénieur Linux Embarqué accro à vim. Bidouille, bricolage, hacking, systèmes embarqués, livres et calembours.',
                language = 'fr',
                author = 'Yoann Sculo',
                github_growl = 'https://github.com/yoannsculo/growl',
                projects_dir = 'projets',
                keywords = 'yoann, sculo, cv, ingénieur systèmes embarqués, ingénieur, systèmes embarqués, blog,  linux, robotique, utt, UTT, linux embarqué, ARM, embarqué, cross-compilation',
        )
