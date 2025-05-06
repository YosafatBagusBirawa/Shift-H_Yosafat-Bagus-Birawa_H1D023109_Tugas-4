% REKOMENDASI GENRE GAME BERDASARKAN PREFERENSI PENGGUNA
% DATABASE
:- dynamic preferensi_pos/1.
:- dynamic preferensi_neg/1.

% FAKTA & ATURAN
genre("RPG").
genre("FPS").
genre("Strategy").
genre("Simulation").
genre("Adventure").

preferensi(karakter_dan_alur_kuat, "RPG").
preferensi(kebebasan_eksplorasi, "RPG").
preferensi(customisasi_karakter, "RPG").

preferensi(aksi_cepattanggapan, "FPS").
preferensi(tantangan_refleks, "FPS").
preferensi(senjata_realistis, "FPS").

preferensi(pemikiran_mendalam, "Strategy").
preferensi(perencanaan_jangka_panjang, "Strategy").
preferensi(atur_unit_dan_sumberdaya, "Strategy").

preferensi(membangun_dunia, "Simulation").
preferensi(realita_virtual, "Simulation").
preferensi(manajemen_sistem, "Simulation").

preferensi(cerita_interaktif, "Adventure").
preferensi(pemecahan_teka_teki, "Adventure").
preferensi(jelajah_lingkungan, "Adventure").

% PERTANYAAN UNTUK PREFERENSI
pertanyaan(karakter_dan_alur_kuat, Y) :-
Y = "apakah kamu suka game dengan karakter kuat dan alur cerita mendalam?".
pertanyaan(kebebasan_eksplorasi, Y) :-
Y = "apakah kamu menikmati kebebasan menjelajahi dunia dalam game?".
pertanyaan(customisasi_karakter, Y) :-
Y = "apakah kamu suka mengatur atau menyesuaikan karakter dalam game?".

pertanyaan(aksi_cepattanggapan, Y) :-
Y = "apakah kamu suka aksi cepat dan membutuhkan reaksi cepat?".
pertanyaan(tantangan_refleks, Y) :-
Y = "apakah kamu menyukai tantangan yang menguji refleks?".
pertanyaan(senjata_realistis, Y) :-
Y = "apakah kamu menyukai game dengan senjata dan efek yang realistis?".

pertanyaan(pemikiran_mendalam, Y) :-
Y = "apakah kamu menikmati permainan yang mengandalkan strategi mendalam?".
pertanyaan(perencanaan_jangka_panjang, Y) :-
Y = "apakah kamu senang menyusun perencanaan jangka panjang dalam game?".
pertanyaan(atur_unit_dan_sumberdaya, Y) :-
Y = "apakah kamu suka mengatur unit dan sumber daya?".

pertanyaan(membangun_dunia, Y) :-
Y = "apakah kamu menyukai game yang memungkinkan untuk membangun sesuatu?".
pertanyaan(realita_virtual, Y) :-
Y = "apakah kamu tertarik dengan game yang menyerupai dunia nyata?".
pertanyaan(manajemen_sistem, Y) :-
Y = "apakah kamu suka mengatur dan mengelola sistem dalam game?".

pertanyaan(cerita_interaktif, Y) :-
Y = "apakah kamu menyukai game dengan cerita yang interaktif?".
pertanyaan(pemecahan_teka_teki, Y) :-
Y = "apakah kamu tertarik pada teka-teki atau puzzle dalam game?".
pertanyaan(jelajah_lingkungan, Y) :-
Y = "apakah kamu menikmati menjelajahi lingkungan di dalam game?".
