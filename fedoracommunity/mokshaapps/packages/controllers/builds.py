# This file is part of Fedora Community.
# Copyright (C) 2008-2010  Red Hat, Inc.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tg import expose, tmpl_context

from moksha.lib.base import Controller
from moksha.lib.helpers import Category, MokshaApp

from helpers import PackagesDashboardContainer

class BuildsDashboard(PackagesDashboardContainer):
    layout = [Category('content-col-apps',
                       MokshaApp('Builds', 'fedoracommunity.builds/table',
                                 params={'filters':{'package':''}}))]

builds_dashboard = BuildsDashboard('builds_dashboard')

class BuildsController(Controller):
    @expose('mako:moksha.templates.widget')
    def index(self, package):
        tmpl_context.widget = builds_dashboard
        return {'options':{'package': package}}