-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 13 Jun 2020 pada 00.20
-- Versi server: 10.1.38-MariaDB
-- Versi PHP: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_smo`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `account_profile`
--

CREATE TABLE `account_profile` (
  `id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `account_profile`
--

INSERT INTO `account_profile` (`id`, `first_name`, `last_name`, `user_id`, `username`) VALUES
(1, 'q', 'q', 1, 'q');

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add profile', 7, 'add_profile'),
(26, 'Can change profile', 7, 'change_profile'),
(27, 'Can delete profile', 7, 'delete_profile'),
(28, 'Can view profile', 7, 'view_profile'),
(29, 'Can add data', 8, 'add_data'),
(30, 'Can change data', 8, 'change_data'),
(31, 'Can delete data', 8, 'delete_data'),
(32, 'Can view data', 8, 'view_data'),
(33, 'Can add training svm seq', 9, 'add_trainingsvmseq'),
(34, 'Can change training svm seq', 9, 'change_trainingsvmseq'),
(35, 'Can delete training svm seq', 9, 'delete_trainingsvmseq'),
(36, 'Can view training svm seq', 9, 'view_trainingsvmseq'),
(37, 'Can add training naive bayes', 10, 'add_trainingnaivebayes'),
(38, 'Can change training naive bayes', 10, 'change_trainingnaivebayes'),
(39, 'Can delete training naive bayes', 10, 'delete_trainingnaivebayes'),
(40, 'Can view training naive bayes', 10, 'view_trainingnaivebayes'),
(41, 'Can add training svm smo', 11, 'add_trainingsvmsmo'),
(42, 'Can change training svm smo', 11, 'change_trainingsvmsmo'),
(43, 'Can delete training svm smo', 11, 'delete_trainingsvmsmo'),
(44, 'Can view training svm smo', 11, 'view_trainingsvmsmo');

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$180000$6lbUeZxGuLZ2$8SkSfBM31sfrL0dvShAq5BgFGVZJw9mN2SpfRt8Q4hQ=', '2020-06-12 10:39:59.305662', 0, 'q', 'q', 'q', '', 0, 1, '2020-05-15 22:27:24.710901');

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'account', 'profile'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'home', 'data'),
(10, 'home', 'trainingnaivebayes'),
(9, 'home', 'trainingsvmseq'),
(11, 'home', 'trainingsvmsmo'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-05-15 21:18:29.123111'),
(2, 'auth', '0001_initial', '2020-05-15 21:18:29.453756'),
(3, 'account', '0001_initial', '2020-05-15 21:18:30.505766'),
(4, 'account', '0002_profile_username', '2020-05-15 21:18:30.700125'),
(5, 'admin', '0001_initial', '2020-05-15 21:18:31.224895'),
(6, 'admin', '0002_logentry_remove_auto_add', '2020-05-15 21:18:31.411330'),
(7, 'admin', '0003_logentry_add_action_flag_choices', '2020-05-15 21:18:31.420305'),
(8, 'contenttypes', '0002_remove_content_type_name', '2020-05-15 21:18:31.555776'),
(9, 'auth', '0002_alter_permission_name_max_length', '2020-05-15 21:18:31.647167'),
(10, 'auth', '0003_alter_user_email_max_length', '2020-05-15 21:18:31.985784'),
(11, 'auth', '0004_alter_user_username_opts', '2020-05-15 21:18:31.996774'),
(12, 'auth', '0005_alter_user_last_login_null', '2020-05-15 21:18:32.058098'),
(13, 'auth', '0006_require_contenttypes_0002', '2020-05-15 21:18:32.063194'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2020-05-15 21:18:32.073247'),
(15, 'auth', '0008_alter_user_username_max_length', '2020-05-15 21:18:32.165648'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2020-05-15 21:18:32.258007'),
(17, 'auth', '0010_alter_group_name_max_length', '2020-05-15 21:18:32.356800'),
(18, 'auth', '0011_update_proxy_permissions', '2020-05-15 21:18:32.367838'),
(19, 'home', '0001_initial', '2020-05-15 21:18:32.483490'),
(20, 'sessions', '0001_initial', '2020-05-15 21:18:32.569942'),
(21, 'home', '0002_trainingnaivebayes', '2020-05-15 23:02:37.888411'),
(22, 'home', '0003_trainingsvmsmo', '2020-06-05 19:25:28.479117'),
(23, 'home', '0004_trainingsvmsmo_epsilon', '2020-06-06 08:19:40.617590');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('21aoajqzko1jt4p6yc8l4xrbkgagn9ei', 'YWZmZjAwMjk1ZWI4ZWMwYmE4ZWVkYjYyYTBiZGIyZGIyM2YxYzQ4Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzAwYTJlNDJlNDY5OThlNjdhYjJiOWQ2YzJhYmY0NDhlOTMyYjRmIiwidXNlcm5hbWUiOiJxIn0=', '2020-06-12 14:24:14.901926'),
('4hrlx33v81p95t2kpr6vgv59i0j9wxyu', 'YWZmZjAwMjk1ZWI4ZWMwYmE4ZWVkYjYyYTBiZGIyZGIyM2YxYzQ4Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzAwYTJlNDJlNDY5OThlNjdhYjJiOWQ2YzJhYmY0NDhlOTMyYjRmIiwidXNlcm5hbWUiOiJxIn0=', '2020-06-26 10:39:59.354123'),
('6t7u81gmczc9uvkwlisqr3yejau310xe', 'YWZmZjAwMjk1ZWI4ZWMwYmE4ZWVkYjYyYTBiZGIyZGIyM2YxYzQ4Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzAwYTJlNDJlNDY5OThlNjdhYjJiOWQ2YzJhYmY0NDhlOTMyYjRmIiwidXNlcm5hbWUiOiJxIn0=', '2020-05-29 22:27:28.353955'),
('9sawqnkt7rmfxnuj1lrlfr12sirwzufx', 'YWZmZjAwMjk1ZWI4ZWMwYmE4ZWVkYjYyYTBiZGIyZGIyM2YxYzQ4Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzAwYTJlNDJlNDY5OThlNjdhYjJiOWQ2YzJhYmY0NDhlOTMyYjRmIiwidXNlcm5hbWUiOiJxIn0=', '2020-06-14 11:53:03.551502'),
('dt7ka36lrwapp0jy7437yx249b75jij6', 'YWZmZjAwMjk1ZWI4ZWMwYmE4ZWVkYjYyYTBiZGIyZGIyM2YxYzQ4Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzAwYTJlNDJlNDY5OThlNjdhYjJiOWQ2YzJhYmY0NDhlOTMyYjRmIiwidXNlcm5hbWUiOiJxIn0=', '2020-06-19 19:18:14.130255'),
('g3p8zlwju0qqm33ae3n8qia3nbm6ggvx', 'YWZmZjAwMjk1ZWI4ZWMwYmE4ZWVkYjYyYTBiZGIyZGIyM2YxYzQ4Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzAwYTJlNDJlNDY5OThlNjdhYjJiOWQ2YzJhYmY0NDhlOTMyYjRmIiwidXNlcm5hbWUiOiJxIn0=', '2020-06-19 11:49:01.508139'),
('itk9jr848ragymikh18dpbgjfkqv26e8', 'YWZmZjAwMjk1ZWI4ZWMwYmE4ZWVkYjYyYTBiZGIyZGIyM2YxYzQ4Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzAwYTJlNDJlNDY5OThlNjdhYjJiOWQ2YzJhYmY0NDhlOTMyYjRmIiwidXNlcm5hbWUiOiJxIn0=', '2020-05-30 12:19:14.140986'),
('k9hjfbv3kalznf6bj1e9qvgowx5jr9d9', 'YWZmZjAwMjk1ZWI4ZWMwYmE4ZWVkYjYyYTBiZGIyZGIyM2YxYzQ4Nzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzAwYTJlNDJlNDY5OThlNjdhYjJiOWQ2YzJhYmY0NDhlOTMyYjRmIiwidXNlcm5hbWUiOiJxIn0=', '2020-06-20 07:58:34.619783');

-- --------------------------------------------------------

--
-- Struktur dari tabel `home_data`
--

CREATE TABLE `home_data` (
  `id` int(50) NOT NULL,
  `semester_mulai` varchar(20) DEFAULT NULL,
  `kode_prodi` varchar(20) DEFAULT NULL,
  `tahun_smstr` varchar(20) DEFAULT NULL,
  `nama_prodi` varchar(150) DEFAULT NULL,
  `peminat_prodi` varchar(100) DEFAULT NULL,
  `rerata_ipk` varchar(100) DEFAULT NULL,
  `kelulusan` varchar(100) DEFAULT NULL,
  `jam_kehadiran_dosen` varchar(100) DEFAULT NULL,
  `rerata_nilai_dosen` varchar(100) DEFAULT NULL,
  `label_kelas` varchar(50) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `home_data`
--

INSERT INTO `home_data` (`id`, `semester_mulai`, `kode_prodi`, `tahun_smstr`, `nama_prodi`, `peminat_prodi`, `rerata_ipk`, `kelulusan`, `jam_kehadiran_dosen`, `rerata_nilai_dosen`, `label_kelas`, `created_at`) VALUES
(1, '20021', '61201', '2014', 'S1_MANAJEMEN_2014', '2.208', '2.3483', '64', '13.7345', '3.282566', 'Berkembang', '2020-05-01 03:41:53.124746'),
(2, '20021', '61201', '2015', 'S1_MANAJEMEN_2015', '2.476', '2.995', '95', '14.9231', '3.227462', 'Berkembang', '2020-05-01 03:41:53.124746'),
(3, '20021', '61201', '2016', 'S1_MANAJEMEN_2016', '0', '3.098', '121', '3.4486', '3.360421', 'Berkembang', '2020-05-01 03:41:53.124746'),
(4, '20021', '61201', '2017', 'S1_MANAJEMEN_2017', '0', '3.111', '193', '3.0061', '3.375515', 'Berkembang', '2020-05-01 03:41:53.124746'),
(5, '20021', '61201', '2018', 'S1_MANAJEMEN_2018', '0', '3.264', '239', '3.4973', '3.396885', 'Berkembang', '2020-05-01 03:41:53.124746'),
(6, '20021', '61201', '2019', 'S1_MANAJEMEN_2019', '0', '0', '368', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(7, '20021', '46201', '2014', 'S1_BIOLOGI_2014', '0.46', '2.457', '14', '15.1509', '2.1226', 'Berkembang', '2020-05-01 03:41:53.124746'),
(8, '20021', '46201', '2015', 'S1_BIOLOGI_2015', '1.05', '2.486', '7', '15.0969', '3.3875', 'Berkembang', '2020-05-01 03:41:53.124746'),
(9, '20021', '46201', '2016', 'S1_BIOLOGI_2016', '0', '5.596', '13', '15.5224', '3.35059', 'Berkembang', '2020-05-01 03:41:53.124746'),
(10, '20021', '46201', '2017', 'S1_BIOLOGI_2017', '0', '2.692', '33', '16', '3.2644', 'Berkembang', '2020-05-01 03:41:53.124746'),
(11, '20021', '46201', '2018', 'S1_BIOLOGI_2018', '0', '2.694', '34', '7.5789', '3.246', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(12, '20021', '46201', '2019', 'S1_BIOLOGI_2019', '0', '0', '57', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(13, '20131', '74105', '2014', 'S2_HUKUM KELUARGA ISLAM_2014', '0.3', '2.891', '0', '14.6087', '3.001304', 'Berkembang', '2020-05-01 03:41:53.124746'),
(14, '20131', '74105', '2015', 'S2_HUKUM KELUARGA ISLAM_2015', '0.266666667', '2.775', '4', '12.6316', '3.310526', 'Berkembang', '2020-05-01 03:41:53.124746'),
(15, '20131', '74105', '2016', 'S2_HUKUM KELUARGA ISLAM_2016', '0.5', '2.954', '2', '12.72', '3.316', 'Berkembang', '2020-05-01 03:41:53.124746'),
(16, '20131', '74105', '2017', 'S2_HUKUM KELUARGA ISLAM_2017', '0', '3.296', '2', '13.2414', '3.3393', 'Berkembang', '2020-05-01 03:41:53.124746'),
(17, '20131', '74105', '2018', 'S2_HUKUM KELUARGA ISLAM_2018', '1', '0', '10', '13.5', '3.13875', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(18, '20131', '74105', '2019', 'S2_HUKUM KELUARGA ISLAM_2019', '0', '0', '0', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(19, '20021', '74101', '2014', 'S1_ILMU HUKUM_2014', '1.148', '2.963', '30', '12.8', '2.9448', 'Berkembang', '2020-05-01 03:41:53.124746'),
(20, '20021', '74101', '2015', 'S1_ILMU HUKUM_2015', '1.116', '3.04', '43', '17.3824', '3.9764', 'Berkembang', '2020-05-01 03:41:53.124746'),
(21, '20021', '74101', '2016', 'S1_ILMU HUKUM_2016', '0.75', '2.88', '58', '20.0233', '3.42907', 'Berkembang', '2020-05-01 03:41:53.124746'),
(22, '20021', '74101', '2017', 'S1_ILMU HUKUM_2017', '0.888888889', '2.84', '67', '21', '2.9715', 'Berkembang', '2020-05-01 03:41:53.124746'),
(23, '20021', '74101', '2018', 'S1_ILMU HUKUM_2018', '0.916666667', '2.923', '62', '17.84', '3.3922', 'Berkembang', '2020-05-01 03:41:53.124746'),
(24, '20021', '74101', '2019', 'S1_ILMU HUKUM_2019', '1.125', '0', '187', '16', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(25, '20021', '63211', '2014', 'S1_ADMINISTRASI BISNIS_2014', '0.593333333', '0', '18', '8.8889', '3.145556', 'Berkembang', '2020-05-01 03:41:53.124746'),
(26, '20021', '63211', '2015', 'S1_ADMINISTRASI BISNIS_2015', '0.713333333', '0', '14', '6.5882', '3.661765', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(27, '20021', '63211', '2016', 'S1_ADMINISTRASI BISNIS_2016', '0.713333333', '0', '15', '16', '3.290345', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(28, '20021', '63211', '2017', 'S1_ADMINISTRASI BISNIS_2017', '1.033333333', '0', '31', '16', '3.310313', 'Berkembang', '2020-05-01 03:41:53.124746'),
(29, '20021', '63211', '2018', 'S1_ADMINISTRASI BISNIS_2018', '0.666666667', '0', '47', '10.3529', '3.509412', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(30, '20021', '63211', '2019', 'S1_ADMINISTRASI BISNIS_2019', '0', '0', '31', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(31, '20021', '88203', '2014', 'S2_PENDIDIKAN BHS INGGRIS_2014', '1.416666667', '0', '168', '16', '3.3264', 'Berkembang', '2020-05-01 03:41:53.124746'),
(32, '20021', '88203', '2015', 'S2_PENDIDIKAN BHS INGGRIS_2015', '1.17', '0', '234', '15.5181', '3.3492', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(33, '20021', '88203', '2016', 'S2_PENDIDIKAN BHS INGGRIS_2016', '1.33', '0', '141', '14.5672', '3.293582', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(34, '20021', '88203', '2017', 'S2_PENDIDIKAN BHS INGGRIS_2017', '0.96', '0', '88', '14.0606', '2.24303', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(35, '20021', '88203', '2018', 'S2_PENDIDIKAN BHS INGGRIS_2018', '0', '0', '110', '15.9286', '3.2525', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(36, '20021', '88203', '2019', 'S2_PENDIDIKAN BHS INGGRIS_2019', '0', '0', '56', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(37, '20181', '48201', '2018', 'S1_FARMASI_2018', '0', '0', '0', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(38, '20181', '48201', '2019', 'S1_FARMASI_2019', '0', '0', '0', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(39, '20141', '88101', '2014', 'S2_PENDIDIKAN BAHASA INDONESIA_2014', '0.775', '3.182', '80', '15.7922', '3.010779', 'Berkembang', '2020-05-01 03:41:53.124746'),
(40, '20141', '88101', '2015', 'S2_PENDIDIKAN BAHASA INDONESIA_2015', '0.37', '3.456', '71', '15.4607', '3.272022', 'Berkembang', '2020-05-01 03:41:53.124746'),
(41, '20141', '88101', '2016', 'S2_PENDIDIKAN BAHASA INDONESIA_2016', '0.875', '3.371', '51', '15.3529', '3.31485', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(42, '20141', '88101', '2017', 'S2_PENDIDIKAN BAHASA INDONESIA_2017', '0.683333333', '3.202', '67', '15.1579', '3.017763', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(43, '20141', '88101', '2018', 'S2_PENDIDIKAN BAHASA INDONESIA_2018', '0.725', '3.21', '39', '15.2381', '3.3969', 'Berkembang', '2020-05-01 03:41:53.124746'),
(44, '20141', '88101', '2019', 'S2_PENDIDIKAN BAHASA INDONESIA_2019', '0', '0', '31', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(45, '20131', '86232', '2014', 'S1_PENDIDIKAN GURU MADRASAH IBTIDAIYAH_2014', '0.7', '3.111', '190', '0', '0', 'Berkembang', '2020-05-01 03:41:53.124746'),
(46, '20131', '86232', '2015', 'S1_PENDIDIKAN GURU MADRASAH IBTIDAIYAH_2015', '0.84', '3.0986', '150', '0', '3.782', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(47, '20131', '86232', '2016', 'S1_PENDIDIKAN GURU MADRASAH IBTIDAIYAH_2016', '0', '3.146', '32', '9.8462', '3.650769', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(48, '20131', '86232', '2017', 'S1_PENDIDIKAN GURU MADRASAH IBTIDAIYAH_2017', '0', '3.072', '31', '7.2727', '3.937273', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(49, '20131', '86232', '2018', 'S1_PENDIDIKAN GURU MADRASAH IBTIDAIYAH_2018', '0', '3.194', '43', '16', '3.811538', 'Berkembang', '2020-05-01 03:41:53.124746'),
(50, '20131', '86232', '2019', 'S1_PENDIDIKAN GURU MADRASAH IBTIDAIYAH_2019', '0', '0', '53', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(51, '20021', '54211', '2014', 'S1_AGROTEKNOLOGI_2014', '0.36', '2.491', '8', '12', '3.28875', 'Berkembang', '2020-05-01 03:41:53.124746'),
(52, '20021', '54211', '2015', 'S1_AGROTEKNOLOGI_2015', '0', '2.607', '10', '8.2308', '3.676923', 'Berkembang', '2020-05-01 03:41:53.124746'),
(53, '20021', '54211', '2016', 'S1_AGROTEKNOLOGI_2016', '1', '2.649', '18', '16', '3.589583', 'Berkembang', '2020-05-01 03:41:53.124746'),
(54, '20021', '54211', '2017', 'S1_AGROTEKNOLOGI_2017', '1', '2.723', '20', '15.2727', '3.411818', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(55, '20021', '54211', '2018', 'S1_AGROTEKNOLOGI_2018', '0', '2.681', '44', '16', '3.41', 'Berkembang', '2020-05-01 03:41:53.124746'),
(56, '20021', '54211', '2019', 'S1_AGROTEKNOLOGI_2019', '0', '0', '30', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(57, '20021', '20201', '2014', 'S1_TEKNIK ELEKTRO_2014', '0.275', '2.369', '22', '15.5769', '2.613077', 'Berkembang', '2020-05-01 03:41:53.124746'),
(58, '20021', '20201', '2015', 'S1_TEKNIK ELEKTRO_2015', '0.325', '2.488', '31', '5.8182', '2.82', 'Berkembang', '2020-05-01 03:41:53.124746'),
(59, '20021', '20201', '2016', 'S1_TEKNIK ELEKTRO_2016', '0', '2.114', '35', '8.5714', '2.691429', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(60, '20021', '20201', '2017', 'S1_TEKNIK ELEKTRO_2017', '0', '2.129', '43', '8.6154', '3.011795', 'Berkembang', '2020-05-01 03:41:53.124746'),
(61, '20021', '20201', '2018', 'S1_TEKNIK ELEKTRO_2018', '0.4', '2.314', '20', '9.9459', '2.814595', 'Berkembang', '2020-05-01 03:41:53.124746'),
(62, '20021', '20201', '2019', 'S1_TEKNIK ELEKTRO_2019', '1', '0', '28', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(63, '20021', '88201', '2014', 'S1_PENDIDIKAN BAHASA & SASTRA INDONESIA_2014', '0.552', '2.698', '43', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(64, '20021', '88201', '2015', 'S1_PENDIDIKAN BAHASA & SASTRA INDONESIA_2015', '0.72', '2.945', '82', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(65, '20021', '88201', '2016', 'S1_PENDIDIKAN BAHASA & SASTRA INDONESIA_2016', '0', '2.794', '48', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(66, '20021', '88201', '2017', 'S1_PENDIDIKAN BAHASA & SASTRA INDONESIA_2017', '0', '2.937', '70', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(67, '20021', '88201', '2018', 'S1_PENDIDIKAN BAHASA & SASTRA INDONESIA_2018', '0', '3.018', '82', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(68, '20021', '88201', '2019', 'S1_PENDIDIKAN BAHASA & SASTRA INDONESIA_2019', '0', '0', '72', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(69, '20131', '74230', '2014', 'S1_HUKUM KELUARGA (AHWAL SYAKHSHIYAH)_2014', '0.4', '3.112', '6', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(70, '20131', '74230', '2015', 'S1_HUKUM KELUARGA (AHWAL SYAKHSHIYAH)_2015', '0.5', '2.975', '11', '0', '2.678333', 'Berkembang', '2020-05-01 03:41:53.124746'),
(71, '20131', '74230', '2016', 'S1_HUKUM KELUARGA (AHWAL SYAKHSHIYAH)_2016', '0', '3.05', '13', '11.4545', '3', 'Berkembang', '2020-05-01 03:41:53.124746'),
(72, '20131', '74230', '2017', 'S1_HUKUM KELUARGA (AHWAL SYAKHSHIYAH)_2017', '0', '3.001', '13', '8', '3.527143', 'Berkembang', '2020-05-01 03:41:53.124746'),
(73, '20131', '74230', '2018', 'S1_HUKUM KELUARGA (AHWAL SYAKHSHIYAH)_2018', '0', '3.232', '26', '0', '3.5', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(74, '20131', '74230', '2019', 'S1_HUKUM KELUARGA (AHWAL SYAKHSHIYAH)_2019', '0', '0', '23', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(75, '20171', '61206', '2017', 'S1_PERBANKAN SYARIAH_2017', '0', '3.123', '0', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(76, '20171', '61206', '2018', 'S1_PERBANKAN SYARIAH_2018', '1.25', '3.187', '0', '7.2727', '3.31', 'Berkembang', '2020-05-01 03:41:53.124746'),
(77, '20171', '61206', '2019', 'S1_PERBANKAN SYARIAH_2019', '0', '0', '0', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(78, '20141', '86233', '2014', 'S1_PENDIDIKAN GURU RAUDHATUL ATHFAL_2014', '0.18', '1.521', '0', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(79, '20141', '86233', '2015', 'S1_PENDIDIKAN GURU RAUDHATUL ATHFAL_2015', '0.38', '2.863', '0', '12.8', '3.30933', 'Berkembang', '2020-05-01 03:41:53.124746'),
(80, '20141', '86233', '2016', 'S1_PENDIDIKAN GURU RAUDHATUL ATHFAL_2016', '0', '3.004', '0', '10.4615', '3.255385', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(81, '20141', '86233', '2017', 'S1_PENDIDIKAN GURU RAUDHATUL ATHFAL_2017', '0', '2.63', '0', '16', '3.46933', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(82, '20141', '86233', '2018', 'S1_PENDIDIKAN GURU RAUDHATUL ATHFAL_2018', '0', '3.351', '4', '16', '3.70875', 'Berkembang', '2020-05-01 03:41:53.124746'),
(83, '20141', '86233', '2019', 'S1_PENDIDIKAN GURU RAUDHATUL ATHFAL_2019', '0', '0', '19', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(84, '20021', '74101', '2014', 'S2_ILMU HUKUM_2014', '0.57', '19.828', '35', '0', '0', 'Berkembang', '2020-05-01 03:41:53.124746'),
(85, '20021', '74101', '2015', 'S2_ILMU HUKUM_2015', '0.2', '3.319', '49', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(86, '20021', '74101', '2016', 'S2_ILMU HUKUM_2016', '0', '2.994', '28', '0', '3.73', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(87, '20021', '74101', '2017', 'S2_ILMU HUKUM_2017', '0', '2.738', '26', '0', '3.1725', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(88, '20021', '74101', '2018', 'S2_ILMU HUKUM_2018', '0.4', '0.531', '42', '8', '3.52', 'Berkembang', '2020-05-01 03:41:53.124746'),
(89, '20021', '74101', '2019', 'S2_ILMU HUKUM_2019', '0', '0', '26', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(90, '20101', '63101', '2014', 'S2_ILMU ADMINISTRASI_2014', '0.08', '2.094', '24', '14.5455', '3.051364', 'Berkembang', '2020-05-01 03:41:53.124746'),
(91, '20101', '63101', '2015', 'S2_ILMU ADMINISTRASI_2015', '0.07', '3.208', '0', '14.7143', '3.167857', 'Berkembang', '2020-05-01 03:41:53.124746'),
(92, '20101', '63101', '2016', 'S2_ILMU ADMINISTRASI_2016', '0', '3.436', '11', '17.75', '3.35425', 'Berkembang', '2020-05-01 03:41:53.124746'),
(93, '20101', '63101', '2017', 'S2_ILMU ADMINISTRASI_2017', '0', '2.411', '4', '15.75', '3.246563', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(94, '20101', '63101', '2018', 'S2_ILMU ADMINISTRASI_2018', '0', '3.09', '2', '15.5', '3.213438', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(95, '20101', '63101', '2019', 'S2_ILMU ADMINISTRASI_2019', '0', '0', '6', '16', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(96, '20021', '54201', '2014', 'S1_AGRIBISNIS_2014', '0.52', '2.665', '2', '7.7037', '3.292593', 'Berkembang', '2020-05-01 03:41:53.124746'),
(97, '20021', '54201', '2015', 'S1_AGRIBISNIS_2015', '0.56', '2.767', '12', '11.6136', '3.621818', 'Berkembang', '2020-05-01 03:41:53.124746'),
(98, '20021', '54201', '2016', 'S1_AGRIBISNIS_2016', '0.833333333', '2.821', '15', '15.8367', '3.547959', 'Berkembang', '2020-05-01 03:41:53.124746'),
(99, '20021', '54201', '2017', 'S1_AGRIBISNIS_2017', '1', '2.939', '15', '15.5224', '3.486418', 'Berkembang', '2020-05-01 03:41:53.124746'),
(100, '20021', '54201', '2018', 'S1_AGRIBISNIS_2018', '0', '3.029', '36', '15.7838', '3.46', 'Berkembang', '2020-05-01 03:41:53.124746'),
(101, '20021', '54201', '2019', 'S1_AGRIBISNIS_2019', '0', '0', '65', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(102, '20131', '86208', '2014', 'S1_PENDIDIKAN AGAMA ISLAM_2014', '0.844', '2.915', '215', '14.2222', '3.048056', 'Berkembang', '2020-05-01 03:41:53.124746'),
(103, '20131', '86208', '2015', 'S1_PENDIDIKAN AGAMA ISLAM_2015', '1.144', '2.872', '254', '15.4286', '3.33125', 'Berkembang', '2020-05-01 03:41:53.124746'),
(104, '20131', '86208', '2016', 'S1_PENDIDIKAN AGAMA ISLAM_2016', '0', '2.979', '144', '8.9143', '3.270286', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(105, '20131', '86208', '2017', 'S1_PENDIDIKAN AGAMA ISLAM_2017', '0', '2.798', '139', '8.1778', '2.976667', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(106, '20131', '86208', '2018', 'S1_PENDIDIKAN AGAMA ISLAM_2018', '0', '3.0897', '116', '14.2651', '3.134699', 'Berkembang', '2020-05-01 03:41:53.124746'),
(107, '20131', '86208', '2019', 'S1_PENDIDIKAN AGAMA ISLAM_2019', '0', '0', '168', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(108, '20021', '88203', '2014', 'S1_PENDIDIKAN BAHASA INGGRIS_2014', '0.765', '4.987', '121', '15.4182', '3.349455', 'Berkembang', '2020-05-01 03:41:53.124746'),
(109, '20021', '88203', '2015', 'S1_PENDIDIKAN BAHASA INGGRIS_2015', '0.755', '2.97', '115', '14.5743', '2.821584', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(110, '20021', '88203', '2016', 'S1_PENDIDIKAN BAHASA INGGRIS_2016', '0', '2.467', '84', '14.4651', '3.116899', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(111, '20021', '88203', '2017', 'S1_PENDIDIKAN BAHASA INGGRIS_2017', '0', '2.57', '95', '13.7521', '2.426446', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(112, '20021', '88203', '2018', 'S1_PENDIDIKAN BAHASA INGGRIS_2018', '0.86', '2.622', '86', '13.0909', '3.409636', 'Berkembang', '2020-05-01 03:41:53.124746'),
(113, '20021', '88203', '2019', 'S1_PENDIDIKAN BAHASA INGGRIS_2019', '0', '0', '64', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(114, '20131', '86008', '2014', 'S3_PENDIDIKAN AGAMA ISLAM_2014', '0.14', '3', '0', '16', '2.985', 'Berkembang', '2020-05-01 03:41:53.124746'),
(115, '20131', '86008', '2015', 'S3_PENDIDIKAN AGAMA ISLAM_2015', '0.233333333', '3.168', '0', '16', '3.8', 'Berkembang', '2020-05-01 03:41:53.124746'),
(116, '20131', '86008', '2016', 'S3_PENDIDIKAN AGAMA ISLAM_2016', '0.8', '3.302', '1', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(117, '20131', '86008', '2017', 'S3_PENDIDIKAN AGAMA ISLAM_2017', '0', '3.281', '0', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(118, '20131', '86008', '2018', 'S3_PENDIDIKAN AGAMA ISLAM_2018', '0.22', '3.234', '3', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(119, '20131', '86008', '2019', 'S3_PENDIDIKAN AGAMA ISLAM_2019', '0', '0', '8', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(120, '20051', '61101', '2014', 'S2_MANAJEMEN_2014', '0.31', '3.002', '9', '16', '3.02', 'Berkembang', '2020-05-01 03:41:53.124746'),
(121, '20051', '61101', '2015', 'S2_MANAJEMEN_2015', '0.16', '3.421', '21', '16', '3.097778', 'Berkembang', '2020-05-01 03:41:53.124746'),
(122, '20051', '61101', '2016', 'S2_MANAJEMEN_2016', '0', '3.198', '34', '2.4615', '3.226923', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(123, '20051', '61101', '2017', 'S2_MANAJEMEN_2017', '0', '2.356', '25', '0', '3.397778', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(124, '20051', '61101', '2018', 'S2_MANAJEMEN_2018', '0.15', '3.916', '20', '7.1111', '3.625556', 'Berkembang', '2020-05-01 03:41:53.124746'),
(125, '20051', '61101', '2019', 'S2_MANAJEMEN_2019', '0', '0', '20', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(126, '20211', '54131', '2014', 'S2_PETERNAKAN_2014', '0', '0', '0', '16', '3.13', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(127, '20211', '54131', '2015', 'S2_PETERNAKAN_2015', '0.55', '3.756', '0', '16', '3.332', 'Berkembang', '2020-05-01 03:41:53.124746'),
(128, '20211', '54131', '2016', 'S2_PETERNAKAN_2016', '0.35', '3.312', '0', '16', '3.456', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(129, '20211', '54131', '2017', 'S2_PETERNAKAN_2017', '0', '2.105', '1', '16', '3.5', 'Berkembang', '2020-05-01 03:41:53.124746'),
(130, '20211', '54131', '2018', 'S2_PETERNAKAN_2018', '0.5', '3.746', '1', '16', '3.544167', 'Berkembang', '2020-05-01 03:41:53.124746'),
(131, '20211', '54131', '2019', 'S2_PETERNAKAN_2019', '0.5', '0', '2', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(132, '20021', '62201', '2014', 'S1_AKUNTANSI_2014', '1.012', '2.673', '72', '15.0857', '3.078', 'Berkembang', '2020-05-01 03:41:53.124746'),
(133, '20021', '62201', '2015', 'S1_AKUNTANSI_2015', '1.116', '2.998', '86', '16', '3.226944', 'Berkembang', '2020-05-01 03:41:53.124746'),
(134, '20021', '62201', '2016', 'S1_AKUNTANSI_2016', '0', '3.098', '76', '7.3333', '3.404167', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(135, '20021', '62201', '2017', 'S1_AKUNTANSI_2017', '0', '3.171', '106', '8.7742', '3.289677', 'Berkembang', '2020-05-01 03:41:53.124746'),
(136, '20021', '62201', '2018', 'S1_AKUNTANSI_2018', '0.8', '3.217', '188', '9.0612', '3.344286', 'Berkembang', '2020-05-01 03:41:53.124746'),
(137, '20021', '62201', '2019', 'S1_AKUNTANSI_2019', '0', '0', '179', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(138, '20021', '22201', '2014', 'S1_TEKNIK SIPIL_2014', '1', '2.466', '9', '16', '2.625455', 'Berkembang', '2020-05-01 03:41:53.124746'),
(139, '20021', '22201', '2015', 'S1_TEKNIK SIPIL_2015', '1.22', '2.425', '9', '8', '2.7218', 'Berkembang', '2020-05-01 03:41:53.124746'),
(140, '20021', '22201', '2016', 'S1_TEKNIK SIPIL_2016', '0', '2.344', '14', '10.1333', '2.840167', 'Berkembang', '2020-05-01 03:41:53.124746'),
(141, '20021', '22201', '2017', 'S1_TEKNIK SIPIL_2017', '0', '2.223', '12', '16.7901', '2.812222', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(142, '20021', '22201', '2018', 'S1_TEKNIK SIPIL_2018', '0.927272727', '2.591', '33', '17.5978', '2.684783', 'Berkembang', '2020-05-01 03:41:53.124746'),
(143, '20021', '22201', '2019', 'S1_TEKNIK SIPIL_2019', '0', '0', '26', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(144, '20131', '11901', '2014', 'PROFESI_PROFESI DOKTER_ 2014', '0.77', '2.979', '45', '16', '3.035', 'Berkembang', '2020-05-01 03:41:53.124746'),
(145, '20131', '11901', '2015', 'PROFESI_PROFESI DOKTER_ 2015', '0.26', '2.82', '44', '16', '2.955', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(146, '20131', '11901', '2016', 'PROFESI_PROFESI DOKTER_ 2016', '0', '2.372', '59', '16', '2.82', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(147, '20131', '11901', '2017', 'PROFESI_PROFESI DOKTER_ 2017', '0', '2.633', '39', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(148, '20131', '11901', '2018', 'PROFESI_PROFESI DOKTER_ 2018', '0.952', '0', '68', '16', '2.112', 'Berkembang', '2020-05-01 03:41:53.124746'),
(149, '20131', '11901', '2019', 'PROFESI_PROFESI DOKTER_ 2019', '0', '0', '58', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(150, '20161', '74102', '2016', 'S2_KENOTARIATAN_2016', '0.471428571', '0', '0', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(151, '20161', '74102', '2017', 'S2_KENOTARIATAN_2017', '1', '0', '0', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(152, '20161', '74102', '2018', 'S2_KENOTARIATAN_2018', '0.533333333', '0', '20', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(153, '20161', '74102', '2019', 'S2_KENOTARIATAN_2019', '0', '0', '21', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(154, '20021', '54231', '2014', 'S1_PETERNAKAN_2014', '0.8', '2.427', '42', '16', '3.16733', 'Berkembang', '2020-05-01 03:41:53.124746'),
(155, '20021', '54231', '2015', 'S1_PETERNAKAN_2015', '1', '2.638', '22', '16', '3.2044', 'Berkembang', '2020-05-01 03:41:53.124746'),
(156, '20021', '54231', '2016', 'S1_PETERNAKAN_2016', '1', '2.481', '35', '16', '3.266071', 'Berkembang', '2020-05-01 03:41:53.124746'),
(157, '20021', '54231', '2017', 'S1_PETERNAKAN_2017', '0.933333333', '2.199', '36', '16', '3.162333', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(158, '20021', '54231', '2018', 'S1_PETERNAKAN_2018', '0.705', '2.215', '30', '16', '2.936875', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(159, '20021', '54231', '2019', 'S1_PETERNAKAN_2019', '1', '0', '58', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(160, '20021', '63201', '2014', 'S1_ILMU ADMINISTRASI NEGARA_2014', '0.613333333', '3.081', '18', '14.95', '3.27475', 'Berkembang', '2020-05-01 03:41:53.124746'),
(161, '20021', '63201', '2015', 'S1_ILMU ADMINISTRASI NEGARA_2015', '0.986666667', '2.91', '29', '1.28', '3.3224', 'Berkembang', '2020-05-01 03:41:53.124746'),
(162, '20021', '63201', '2016', 'S1_ILMU ADMINISTRASI NEGARA_2016', '0', '3.059', '39', '1.1852', '3.38222', 'Berkembang', '2020-05-01 03:41:53.124746'),
(163, '20021', '63201', '2017', 'S1_ILMU ADMINISTRASI NEGARA_2017', '0', '3.094', '56', '4.6377', '3.695217', 'Berkembang', '2020-05-01 03:41:53.124746'),
(164, '20021', '63201', '2018', 'S1_ILMU ADMINISTRASI NEGARA_2018', '0', '3', '77', '1.0811', '3.406081', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(165, '20021', '63201', '2019', 'S1_ILMU ADMINISTRASI NEGARA_2019', '0', '0', '84', '0', '0', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(166, '20131', '86131', '2014', 'S2_PENDIDIKAN AGAMA ISLAM_2014', '0.91', '0', '79', '16', '3.160488', 'Berkembang', '2020-05-01 03:41:53.124746'),
(167, '20131', '86131', '2015', 'S2_PENDIDIKAN AGAMA ISLAM_2015', '0.3', '0', '24', '13.6', '3.27375', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(168, '20131', '86131', '2016', 'S2_PENDIDIKAN AGAMA ISLAM_2016', '0.8', '0', '67', '8.2286', '3.430571', 'Berkembang', '2020-05-01 03:41:53.124746'),
(169, '20131', '86131', '2017', 'S2_PENDIDIKAN AGAMA ISLAM_2017', '0', '0', '92', '5.6', '2.7105', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(170, '20131', '86131', '2018', 'S2_PENDIDIKAN AGAMA ISLAM_2018', '0', '0', '23', '14.5778', '3.1233', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(171, '20021', '21201', '2014', 'S1_TEKNIK MESIN_2014', '0.62', '2.399', '23', '0', '2.436', 'Berkembang', '2020-05-01 03:41:53.124746'),
(172, '20021', '21201', '2015', 'S1_TEKNIK MESIN_2015', '0.693333333', '2.456', '16', '1.1163', '2.833488', 'Berkembang', '2020-05-01 03:41:53.124746'),
(173, '20021', '21201', '2016', 'S1_TEKNIK MESIN_2016', '0', '2.139', '30', '0', '2.6196', 'Belum Berkembang', '2020-05-01 03:41:53.124746'),
(174, '20021', '21201', '2017', 'S1_TEKNIK MESIN_2017', '0', '2.166', '36', '0.9846', '2.812154', 'Berkembang', '2020-05-01 03:41:53.124746');

-- --------------------------------------------------------

--
-- Struktur dari tabel `home_trainingnaivebayes`
--

CREATE TABLE `home_trainingnaivebayes` (
  `id` int(11) NOT NULL,
  `k_fold` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `home_trainingnaivebayes`
--

INSERT INTO `home_trainingnaivebayes` (`id`, `k_fold`) VALUES
(1, '5');

-- --------------------------------------------------------

--
-- Struktur dari tabel `home_trainingsvmseq`
--

CREATE TABLE `home_trainingsvmseq` (
  `id` int(11) NOT NULL,
  `lamda` varchar(100) DEFAULT NULL,
  `sigma` varchar(100) DEFAULT NULL,
  `constant` varchar(100) DEFAULT NULL,
  `gamma` varchar(100) DEFAULT NULL,
  `iterasi` varchar(100) DEFAULT NULL,
  `k_fold` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `home_trainingsvmseq`
--

INSERT INTO `home_trainingsvmseq` (`id`, `lamda`, `sigma`, `constant`, `gamma`, `iterasi`, `k_fold`) VALUES
(1, NULL, NULL, '1.0', '0.01', '100', '7');

-- --------------------------------------------------------

--
-- Struktur dari tabel `home_trainingsvmsmo`
--

CREATE TABLE `home_trainingsvmsmo` (
  `id` int(11) NOT NULL,
  `constant` varchar(100) DEFAULT NULL,
  `iterasi` varchar(100) DEFAULT NULL,
  `k_fold` varchar(100) DEFAULT NULL,
  `epsilon` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `home_trainingsvmsmo`
--

INSERT INTO `home_trainingsvmsmo` (`id`, `constant`, `iterasi`, `k_fold`, `epsilon`) VALUES
(1, '1.0', '1000', '5', '0.0001');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `account_profile`
--
ALTER TABLE `account_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indeks untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indeks untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indeks untuk tabel `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeks untuk tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indeks untuk tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indeks untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indeks untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indeks untuk tabel `home_data`
--
ALTER TABLE `home_data`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `home_trainingnaivebayes`
--
ALTER TABLE `home_trainingnaivebayes`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `home_trainingsvmseq`
--
ALTER TABLE `home_trainingsvmseq`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `home_trainingsvmsmo`
--
ALTER TABLE `home_trainingsvmsmo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `account_profile`
--
ALTER TABLE `account_profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT untuk tabel `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT untuk tabel `home_data`
--
ALTER TABLE `home_data`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=175;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `account_profile`
--
ALTER TABLE `account_profile`
  ADD CONSTRAINT `account_profile_user_id_bdd52018_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
