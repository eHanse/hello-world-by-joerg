# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limted T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from gevent import subprocess
from openerp import models, api, fields
from subprocess import Popen, PIPE, STDOUT


class ThreemaSubprocess(models.Model):

    message = "Hallo Joerg. Diese Nachr..."
    receiver = "77W2BCK2"
    sender= "*OATRADE"
    api_key = "fOUJ2oQw2Y2lk8ri"
    priv_path = "******************************"

    #compile shell command; encode message as bystring
    commandstring = 'threema-gateway send_e2e'
    commandstring = commandstring + receiver + '' + sender + '' + api_key + '' + priv_path
    byte_msg = message.encode(encoding='utf-8')

    process = subprocess.Popen(commandstring, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
    stdout = process.communicate(input=byte_msg)[0]

    @api.multi
    def write(self, vals):
        return

    @api.model
    def create(self,vals):
        return