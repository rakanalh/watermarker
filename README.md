NOTE
====

All credits for the development of this package go to [Pavel Zhukov](https://bitbucket.org/zeus/)

Watermarker
===========

Library for add text watermarks to images using PIL

Installation:
=============

* Install with pip or easy install (All dependencies will be installed automatically)


Usage:
======

Import watermark function from watermarker, then call watermark, providing options:

* image (required) - PIL Image instance
* text (required)- text to add over image
* font_path (required)- font that will be used
* font_scale (required or font_size provided) - watermark font size will be set as percent of image height
* font_size (required or font_scale provided)
* color (optional) - default (0,0,0)
* opacity (optional) - default 0.6
* margin (optional) - default (30, 30) - margin, in pixels, from bottom right corner of image, where watermark will be placed

sorl-thumbnail integration
--------------------------

Add to your settings::

 THUMBNAIL_ENGINE = 'watermarker.sorl_engine.WatermarkEngine'
 WATERMARK_OPTIONS = {'font_scale': 0.05, 'font_path': PATH_TO_FONT} # Any other options from watermark function
 WATERMARK_MIN_SIZE = 50 #Minimum image size (max(height, width)) to add watermark

You can add::

 WATERMARK_FORCE = u'watermark text' # Add watermark to all images except less than WATERMARK_MIN_SIZE

or add watermark option to thumbnail tag::

 thumbnail image "1000x1000" watermark="my watermark"
