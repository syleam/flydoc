# -*- coding: utf-8 -*-
##############################################################################
#
#    flydoc module for OpenERP, FlyDoc webservices access from OpenERP
#    Copyright (C) 2014 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#
#    This file is a part of flydoc
#
#    flydoc is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    flydoc is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm
from openerp.osv import fields
from pyflydoc import FlyDocSubmissionService


class FlyDocService(orm.Model):
    _name = 'flydoc.service'
    _description = 'FlyDoc Service'

    _columns = {
        'name': fields.char('Name', size=64, required=True, help='Name of the FlyDoc service'),
        'username': fields.char('Username', size=64, required=True, help='Username for login'),
        'password': fields.char('Password', size=64, required=True, help='Password of the user'),
    }


class FlyDocTransport(orm.Model):
    _name = 'flydoc.transport'
    _description = 'FlyDoc Transport'

    _columns = {
        'service_ids': fields.many2many('flydoc.service', 'Services', help='Services from which this transport is available'),
        'transportid': fields.integer('Transport ID', help='Identifier of this transport at FlyDoc'),
        'name': fields.char('Transport Name', size=64, required=True, help='Name of the transport'),
        'var_ids': fields.one2many('flydoc.transport.var', 'transport_id', 'Vars', help='Vars of this transport'),
        'attachment_ids': fields.one2many('flydoc.transport.attachment', 'transport_id', 'Attachments', help='Attachments of this transport'),
    }


class FlyDocTransportVar(orm.Model):
    _name = 'flydoc.transport.var'
    _description = 'FlyDoc Transport Var'

    def _getTransportVarTypes(self):
        return [(typeCode, typeName) for typeName, typeCode in FlyDocSubmissionService().VAR_TYPE]

    _columns = {
        'transport_id': fields.many2one('flydoc.transport', 'Transport', required=True, help='Transport of this var'),
        'name': fields.char('Name', size=64, required=True, help='Name of the var'),
        'value': fields.char('Value', size=64, help='Value of the var'),
        'type': fields.selection(_getTransportVarTypes, 'Type', help='Type of the var'),
    }


class FlyDocTransportAttachment(orm.Model):
    _name = 'flydoc.transport.attachment'
    _description = 'FlyDoc Transport Attachment'

    _columns = {
        'transport_id': fields.many2one('flydoc.transport', 'Transport', required=True, help='Transport of this attachment'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: