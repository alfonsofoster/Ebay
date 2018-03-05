#!/usr/bin/python

import sqlite3
import time
import logging, logging_config

logging_config.log()
logging.info('llegue a writedb')

def writedb(**fields):
        logging.info('entr ----------e a la funcion')
        first_name = fields['first_name']
	last_name = fields['last_name']
	txn_id = fields['txn_id']
	receiver_email = fields['receiver_email']
	payment_status = fields['payment_status']
	tax = fields['tax']
	residence_country = fields['residence_country']
	invoice = fields['invoice']
	address_state = fields['address_state']
	payer_status = fields['payer_status']
	txn_type = fields['txn_type']
	address_street = fields['address_street']
	verify_sign = fields['verify_sign']
	payment_date = fields['payment_date']
	item_name = fields['item_name']
	address_country = fields['address_country']
	custom = fields['custom']
	notify_version = fields['notify_version']
	address_name = fields['address_name']
	for_auction = fields['for_auction']
	mc_gross_1 = fields['mc_gross_1']
	test_ipn = fields['test_ipn']
	logging.info('mitad de funcion')
	item_number = fields['item_number']
	receiver_id = fields['receiver_id']
	business = fields['business']
	payer_id = fields['payer_id']
	auction_closing_date = fields['auction_closing_date']
	auction_buyer_id = fields['auction_buyer_id']
	address_zip = fields['address_zip']
	address_country_code = fields['address_country_code']
	address_city = fields['address_city']
	address_status = fields['address_status']
	mc_fee = fields['mc_fee']
	mc_currency = fields['mc_currency']
	shipping = fields['shipping']
	payer_email = fields['payer_email']
	payment_type = fields['payment_type']
	mc_gross = fields['mc_gross']
	quantity = fields['quantity']
	#trx_date = time.strftime("%c")
        logging.info('tengo a %s', last_name)
        # Creates or opens a file called mydb with a SQLite3 DB
        db = sqlite3.connect('orchestra.db')
        cursor = db.cursor()
        logging.info('voy a meter la data a la bd')
        cursor.execute('''INSERT INTO paypal_data(first_name,last_name,txn_id,receiver_email,payment_status,tax,residence_country,invoice,address_state,payer_status,txn_type,address_street,verify_sign,payment_date,item_name,address_country,custom,notify_version,address_name,for_auction,mc_gross_1,test_ipn,item_number,receiver_id,business,payer_id,auction_closing_date,auction_buyer_id,address_zip,address_country_code,address_city,address_status,mc_fee,mc_currency,shipping,payer_email,payment_type,mc_gross,quantity) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(first_name,last_name,txn_id,receiver_email,payment_status,tax,residence_country,invoice,address_state,payer_status,txn_type,address_street,verify_sign,payment_date,item_name,address_country,custom,notify_version,address_name,for_auction,mc_gross_1,test_ipn,item_number,receiver_id,business,payer_id,auction_closing_date,auction_buyer_id,address_zip,address_country_code,address_city,address_status,mc_fee,mc_currency,shipping,payer_email,payment_type,mc_gross,quantity))
        #cursor.execute('''INSERT INTO paypal_data(first_name,last_name,txn_id,receiver_email,payment_status) VALUES(?,?,?,?,?)''',(first_name,last_name,txn_id,receiver_email,payment_status))
        logging.info('ya sali y voy a commit')
        db.commit()
        logging.info('ya commit ahora cerrare')
        db.close() 
        logging.info('ya cerre, voy a retornar')       
        return;
