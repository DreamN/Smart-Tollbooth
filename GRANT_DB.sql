CREATE USER pjuser WITH PASSWORD 'random';
ALTER ROLE pjuser SET client_encoding TO 'utf8';
ALTER ROLE pjuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE pjuser SET timezone TO 'Asia/Bangkok';
GRANT ALL PRIVILEGES ON DATABASE smarttb TO pjuser;
