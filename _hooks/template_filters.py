# vim:syntax=python:sw=4:ts=4:expandtab
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Rico Schiekel (fire at downgra dot de)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#

import re
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

@templateFilter
def dateFormat(dt, format='%d/%m/%Y'):
    return dt.strftime(format)

@templateFilter
def dateFormatFull(dt, format=ur'Le %d/%m/%Y à %H:%M'):
    return dt.strftime(format)

@templateFilter
def yearFormat(dt, format='%Y'):
    return dt.strftime(format)

@templateFilter
def xmldatetime(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

@templateFilter
def strip(s, length=300):
    return striphtml(str(s[:length]))+"..."

@templateFilter
def slugify(inStr):
    removelist = ["a", "an", "as", "at", "before", "but", "by", "for","from","is", "in", "into", "like", "of", "off", "on", "onto","per","since", "than", "the", "this", "that", "to", "up", "via","with"];
    for a in removelist:
        aslug = re.sub(r'\b'+a+r'\b','',inStr)
    aslug = re.sub('[^\w\s-]', '', aslug).strip().lower()
    aslug = re.sub('\s+', '-', aslug)
    return aslug
