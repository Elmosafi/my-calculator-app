[app]
title = My Calculator
package.name = calculator
package.domain = org.elmosafi

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy

orientation = portrait

[buildozer]
log_level = 2

[app]
android.permissions = INTERNET
android.api = 28
android.minapi = 21
