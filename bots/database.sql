CREATE TABLE `politicos` (
  `id` bigint(25) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `handle` varchar(45) DEFAULT NULL,
  `seguidores` int(25) DEFAULT NULL,
  `buscar` int(1) DEFAULT NULL,
  `grafo` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `seguidores` (
  `id` bigint(25) NOT NULL,
  `probabilidade` double DEFAULT NULL,
  `data_criacao` datetime DEFAULT NULL,
  `handle` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `prob` (`probabilidade`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `politicos_seguidores` (
  `idpoliticos_seguidores` bigint(25) NOT NULL AUTO_INCREMENT,
  `id_politico` bigint(25) NOT NULL,
  `id_seguidor` bigint(25) NOT NULL,
  `pos_seguidor` bigint(25) DEFAULT NULL,
  PRIMARY KEY (`idpoliticos_seguidores`),
  KEY `IDPOL` (`id_politico`) USING BTREE,
  KEY `IDSEG` (`id_seguidor`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
