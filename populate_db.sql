-- CREATE TABLE IF NOT EXISTS usuarios (
--     id_usuario          bigserial           PRIMARY KEY,
--     nome                varchar(255)        NOT NULL,
--     username            varchar(255)        NOT NULL UNIQUE,
--     senha               varchar(255)        NOT NULL,
-- );

-- CREATE TABLE IF NOT EXISTS empresa_maritima (
--     id_empresa_maritma      bigserial               PRIMARY KEY,
--     data_criacao            date                    NOT NULL,
--     nome_fantasia           varchar(255)            NOT NULL UNIQUE,
--     id_usuario              integer                 NOT NULL REFERENCES usuarios(id_usuario)
-- );

-- CREATE TABLE IF NOT EXISTS containers (
--     id_container            bigserial               PRIMARY KEY,
--     codigo_ratreio          integer                 NOT NULL,
--     teu                     integer                 NOT NULL DEFAULT=1,
--     Tipo                    varchar(255)            NOT NULL DEFAULT='DRY BOX',
--     id_empresa_maritima     integer                 NOT NULL REFERENCES empresa_maritima(id_empresa_maritima)
-- );

-- CREATE TABLE IF NOT EXISTS navios (
--     id_navio                bigserial               PRIMARY KEY,
--     nome                    varchar(256)            NOT NULL UNIQUE,
--     calado                  integer                 NOT NULL,
--     tamanho                 integer                 NOT NULL,
--     nacionalidade           varchar(50)             NOT NULL,
--     id_empresa_maritima     integer                 NOT NULL REFERENCES empresa_maritima(id_empresa_maritima)
-- );

-- CREATE TABLE IF NOT EXISTS viagem (
--     id_viagem               bigserial               PRIMARY KEY,
--     destino                 varchar(256)            NOT NULL,
--     codigo                  integer                 NOT NULL UNIQUE,
--     id_navio                integer                 NOT NULL REFERENCES navios(id_navio),
-- );

-- CREATE TABLE IF NOT EXISTS container_viagem (
--     id_container_viagem     bigserial               PRIMARY KEY,
--     data_criacao            date                    NOT NULL,
--     ultima_atualizacao      date                    NOT NULL,
--     id_container            integer                 NOT NULL REFERENCES containers(id_container),
--     id_viagem               integer                 NOT NULL REFERENCES viagem(id_viagem),
-- );

-- CREATE TABLE IF NOT EXISTS porto (
--     id_porto                bigserial               PRIMARY KEY,
--     nome                    varchar(255)            NOT NULL UNIQUE,
--     pais                    varchar(255)            NOT NULL,
--     cidade                  varchar(255)            NOT NULL,
--     teus                    integer                 NOT NULL,
--     disponibilidade         integer                 NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS navio_porto (
--     id_navio_porto          bigserial               PRIMARY KEY,
--     data_chegada            date,
--     data_saida              date,
--     id_navio                integer                 NOT NULL REFERENCES navios(id_navio),
--     id_porto                integer                 NOT NULL REFERENCES porto(id_porto),
-- );

-- CREATE TABLE IF NOT EXISTS container_porto (
--     id_container_porto      bigserial               PRIMARY KEY,
--     data_entrada            date                    NOT NULL,
--     data_saida              date,
--     id_container            integer                 NOT NULL REFERENCES containers(id_container),
--     id_porto                integer                 NOT NULL REFERENCES porto(id_porto),
-- );

INSERT INTO usuarios (nome, username, senha)
    VALUES
        ('Marco', 'mcos', 'navio123'),
        ('Chico', 'chimos', 'navio321');

INSERT INTO empresa_maritima (data_criacao, nome_fantasia, id_usuario)
    VALUES
        ('10-10-2010', 'Empresa X', 1),
        ('20-10-2014', 'Empresa Y', 2);

INSERT INTO containers (codigo_rastreio, teu, tipo, id_empresa_maritima)
    VALUES
        (23456, 1, 'DRY BOX', 1),
        (78945, 2, 'DRY BOX', 1),
        (21458, 1, 'DRY BOX', 1),
        (74125, 2, 'DRY BOX', 2),
        (36985, 1, 'DRY BOX', 2),
        (73165, 2, 'DRY BOX', 2);


INSERT INTO navios (nome, calado, tamanho, nacionalidade, id_empresa_maritima)
    VALUES
        ('Navio 1', 10, 20, 'Brasil', 1),
        ('Navio 2', 5, 15, 'Venezuela', 1),
        ('Navio 3', 12, 22, 'Chile', 2),
        ('Navio 4', 20, 30, 'China', 2);

INSERT INTO viagens (destino, codigo, id_navio)
    VALUES
        ('Viagem X', 2040, 1),
        ('Viagem Y', 3085, 1),
        ('Viagem Z', 4587, 2),
        ('Viagem B', 7496, 2);

INSERT INTO container_viagem (data_criacao, ultima_atualizacao, id_container, id_viagem)
    VALUES
        ('02-10-2005', '20-10-2005', 1, 1),
        ('02-08-2010', '30-08-2010', 2, 1),
        ('02-01-2017', '12-01-2017', 3, 2),
        ('02-09-2020', '14-09-2020', 4, 2),
        ('02-04-2000', '01-04-2000', 5, 3),
        ('02-02-2008', '15-02-2008', 6, 3),
        ('02-05-2001', '13-05-2001', 1, 4),
        ('02-12-2019', '22-12-2019', 2, 4);

INSERT INTO porto (nome, pais, cidade, teus, disponibilidade)
    VALUES
        ('Porto X', 'Brasil', 'Blumenal', 50, 50);

INSERT INTO navio_porto (data_chegada, data_saida, id_navio, id_porto)
    VALUES
        ('07-02-2007', '12-10-2007', 1, 1),
        ('07-08-2010', '12-02-2011', 2, 1),
        ('07-03-2012', '12-07-2012', 3, 1),
        ('07-09-2020', '12-11-2020', 4, 1);

INSERT INTO container_porto (data_entrada, data_saida, id_container, id_porto)
    VALUES
        ('01-02-2005', '07-03-2008', 1, 1),
        ('01-02-2005', '07-04-2005', 2, 1),
        ('01-02-2005', '07-04-2005', 3, 1),
        ('01-02-2005', '07-07-2005', 4, 1),
        ('01-02-2005', '07-08-2010', 5, 1),
        ('01-02-2005', '07-05-2005', 6, 1);







