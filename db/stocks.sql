CREATE TABLE stocks (
  `id` integer primary key autoincrement,
  `url_name` varchar(255) NOT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `symbol` varchar(255) NOT NULL,
  `specific_tag` varchar(255) DEFAULT NULL,
  `broad_tag` varchar(255) DEFAULT NULL,
  `region` varchar(255) DEFAULT NULL
);

INSERT INTO `stocks` (`id`, `url_name`, `display_name`, `symbol`, `specific_tag`, `broad_tag`, `region`) VALUES
('1', 'Walmart', 'Walmart', 'wmt', '', 'retail', 'US'),
('2', 'ExxonMobil', 'ExxonMobil', 'xom', 'oil', 'energy', 'worldwide'),
('3', 'Apple', 'Apple', 'aapl', '', '', 'worldwide'),
('5', 'Amazon', 'Amazon', 'amzn', '', 'retail', 'worldwide'),
('6', 'Air-BnB', 'Airbnb', 'ABNB', 'gig economy', 'real estate', 'worldwide'),
('8', 'CVS', 'CVS', 'cvs', 'pharmacy', 'health care', 'US'),
('9', 'AT&T', 'AT&T', 't', '', 'telecomunications', 'US'),
('10', 'AmerisourceBergen', 'AmerisourceBergen', 'abc', '', 'health care', 'US'),
('11', 'Chevron', 'Chevron', 'cvx', 'oil', 'energy', 'US'),
('12', 'Ford', 'Ford', 'f', '', 'automotive', 'worldwide'),
('13', 'General-Motors', 'General Motors', 'gm', '', 'automotive', 'US'),
('14', 'Costco', 'Costco', 'cost', '', 'retail', 'US'),
('15', 'Alphabet', 'Alphabet', 'goog', 'google', 'technology', 'worldwide'),
('16', 'Cardinal-Health', 'Cardinal Health', 'cah', '', 'health care', 'US'),
('17', 'Walgreens-Boots', 'Walgreens Boots', 'wba', 'pharmacy', 'pharmaceuticals', 'worldwide'),
('18', 'JPMorgan-Chase', 'JPMorgan Chase', 'jpm', '', 'financial', 'worldwide'),
('19', 'Verizon', 'Verizon', 'vz', '', 'telecomunications', 'US'),
('20', 'Kroger', 'Kroger', 'kr', '', 'retail', 'US'),
('21', 'General-Electric', 'General Electric', 'ge', '', 'energy', 'US'),
('22', 'Uber', 'Uber', 'uber', 'gig economy', '', 'worldwide'),
('23', 'Lyft', 'Lyft', 'lyft', 'gig economy', '', 'worldwide'),
('25', 'Bank-of-America', 'Bank of America', 'bac', '', 'financial', 'US'),
('26', 'Microsoft', 'Microsoft', 'msft', '', 'technology', 'worldwide'),
('27', 'Home-Depot', 'Home Depot', 'hd', '', 'retail', 'US'),
('28', 'Boeing', 'Boeing', 'ba', '', 'aerospace', 'worldwide'),
('29', 'Wells-Fargo', 'Wells Fargo', 'wfc', '', 'financial', 'US'),
('30', 'Citigroup', 'Citigroup', 'c', '', 'financial', 'worldwide'),
('31', 'Marathon-Petroleum', 'Marathon Petroleum', 'mpc', 'oil', 'energy', 'worldwide'),
('32', 'Comcast', 'Comcast', 'cmcsa', '', 'telecomunications', 'US'),
('33', 'Anthem', 'Anthem', 'antm', '', 'insurance', 'US'),
('34', 'Dell', 'Dell', 'dell', '', 'technology', 'worldwide'),
('35', 'DuPont', 'DuPont', 'dd', '', 'chemicals', 'worldwide'),
('37', 'Johnson&Johnson', 'Johnson & Johnson', 'jnj', '', 'consumer goods', 'worldwide'),
('38', 'IBM', 'IBM', 'ibm', '', 'technology', 'worldwide'),
('39', 'Target', 'Target', 'tgt', '', 'retail', 'US'),
('40', 'Freddie-Mac', 'Freddie-Mac', 'fmcc', '', 'financial', 'US'),
('41', 'United-Parcel-Service', 'UPS', 'ups', 'postal', '', 'US'),
('43', 'Intel', 'Intel', 'intc', '', 'computer hardware', 'worldwide'),
('44', 'MetLife', 'MetLife', 'met', '', 'insurance', 'worldwide'),
('45', 'Procter&Gamble', 'Procter & Gamble', 'pg', '', 'consumer goods', 'worldwide'),
('47', 'FedEx', 'FedEx', 'fdx', 'courier', '', 'US'),
('48', 'PepsiCo', 'PepsiCo', 'pep', '', 'food', 'worldwide'),
('53', 'Walt-Disney', 'Disney', 'dis', 'disney', 'media', 'worldwide'),
('55', 'HP', 'HP', 'hpq', '', 'hardware', 'worldwide'),
('57', 'Facebook', 'Facebook', 'fb', '', 'technology', 'worldwide'),
('60', 'Lockheed-Martin', 'Lockheed Martin', 'lmt', 'military', 'aerospace', 'US'),
('61', 'Pfizer', 'Pfizer', 'pfe', '', 'pharmaceuticals', 'worldwide'),
('62', 'Goldman-Sachs', 'Goldman Sachs', 'gs', '', 'financial', 'worldwide'),
('63', 'Morgan-Stanley', 'Morgan Stanley', 'ms', '', 'financial', 'US'),
('64', 'Cisco', 'Cisco', 'csco', '', 'hardware', 'worldwide'),
('66', 'AIG', 'AIG', 'aig', '', 'insurance', 'worldwide'),
('68', 'American-Airlines', 'American Airlines', 'aal', '', 'aerospace', 'US'),
('69', 'Delta-Air-Lines', 'Delta Air Lines', 'dal', '', 'aerospace', 'US'),
('72', 'American-Express', 'American Express', 'axp', '', 'financial', 'worldwide'),
('74', 'Best-Buy', 'Best Buy', 'bby', '', 'retail', 'US'),
('76', 'Merck', 'Merck', 'mrk', '', 'transport', 'worldwide'),
('77', 'Honeywell-International', 'Honeywell', 'hon', '', 'aerospace', 'US'),
('81', 'Oracle', 'Oracle', 'orcl', '', 'technology', 'worldwide'),
('87', 'Deere', 'Deere', 'de', 'agriculture', 'automotive', 'worldwide'),
('90', 'Nike', 'Nike', 'nke', '', 'clothing', 'worldwide'),
('98', 'Capital-One-Financial', 'Capital One Financial', 'cof', '', 'financial', 'US'),
('100', 'Coca-Cola', 'Coca-Cola', 'ko', '', 'consumer', 'worldwide'),
('102', 'Hewlett-Packard-Enterprise', 'Hewlett-Packard Enterprise', 'hpe', '', 'technology', 'worldwide'),
('104', 'Twenty-First-Century-Fox', 'Twenty-First-Century Fox', '21cenmgm.ns', '', 'media', 'US'),
('110', 'Philip-Morris-International', 'Philip Morris International', 'pm', 'tobacco', '', 'worldwide'),
('117', 'U.S.Bancorp', 'U.S.Bancorp', 'usb-po', '', 'financial', 'US'),
('121', 'Starbucks', 'Starbucks', 'sbux', 'coffee', '', 'worldwide'),
('127', 'Halliburton', 'Halliburton', 'hal', '', 'energy', 'US'),
('134', 'Union-Pacific', 'Union Pacific', 'unp', '', 'transport', 'US'),
('137', 'Qualcomm', 'Qualcomm', 'qcom', '', 'computer hardware', 'worldwide'),
('142', 'Southwest-Airlines', 'Southwest Airlines', 'luv', '', 'aerospace', 'US'),
('144', 'Tesla', 'Tesla', 'tsla', '', 'automotive', 'worldwide'),
('149', 'McDonalds', 'McDonalds', 'mcd', 'fast-food', '', 'worldwide'),
('150', 'Broadcom', 'Broadcom', 'avgo', '', 'hardware', 'worldwide'),
('153', 'Visa', 'Visa', 'v', '', 'financial', 'worldwide'),
('186', 'Gap', 'Gap', 'gps', '', 'textile', 'US'),
('197', 'Netflix', 'Netflix', 'nflx', '', 'media', 'worldwide'),
('240', 'salesforce.com', 'salesforce.com', 'crm', 'CRM', 'technology', 'worldwide'),
('268', 'Nvidia', 'Nvidia', 'nvda', '', 'computer hardware', 'worldwide'),
('295', 'eBay', 'eBay', 'ebay', '', '', 'worldwide'),
('300', 'McKesson', 'McKesson', 'mck', '', 'health care', 'US'),
('411', 'Apache', 'Apache', 'apa', '', 'technology', 'worldwide'),
('416', 'Motorola', 'Motorola', 'msi', '', 'technology', 'worldwide'),
('417', 'Mastercard', 'Mastercard', 'ma', '', 'financial', 'worldwide');
