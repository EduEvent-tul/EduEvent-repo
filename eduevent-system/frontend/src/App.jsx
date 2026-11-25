import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';

// Później zespoły zamienią te zaślepki na importy ze swoich folderów w src/modules/...
const Placeholder = ({ name }) => (
  <div style={{ padding: '20px' }}>
    <h2>{name}</h2>
    <p>Miejsce na komponent zespołu.</p>
  </div>
);

function Navbar() {
  const { user, login, logout } = useAuth();

  return (
    <nav style={{ display: 'flex', gap: '15px', padding: '12px 20px', borderBottom: '1px solid #ccc', alignItems: 'center' }}>
      <strong>EduEvent</strong>
      <Link to="/">Katalog (Discovery)</Link>
      {user?.role === 'organizer' && <Link to="/create-event">+ Dodaj wydarzenie (Events)</Link>}
      {user?.role === 'organizer' && <Link to="/attendance/1">Obecność (Attendance)</Link>}
      {user && <Link to="/my-dashboard">Moje zapisy i powiadomienia</Link>}

      <div style={{ marginLeft: 'auto', display: 'flex', gap: '10px', alignItems: 'center' }}>
        {user ? (
          <>
            <span>{user.email} ({user.role})</span>
            <button onClick={logout}>Wyloguj</button>
          </>
        ) : (
          <>
            <button
              onClick={() => login('test-token', { email: 'organizator@edu.pl', role: 'organizer' })}
              style={{ fontSize: '12px' }}
            >
              [Test: Udawaj Organizatora]
            </button>
            <Link to="/login">Zaloguj się</Link>
          </>
        )}
      </div>
    </nav>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Placeholder name="Katalog wydarzeń (Team 3)" />} />
          <Route path="/login" element={<Placeholder name="Logowanie / Rejestracja (Team 1)" />} />
          <Route path="/create-event" element={<Placeholder name="Tworzenie wydarzenia (Team 2)" />} />
          <Route path="/my-dashboard" element={<Placeholder name="Moje zapisy (Team 4) + Powiadomienia (Team 6)" />} />
          <Route path="/attendance/:eventId" element={<Placeholder name="Lista obecności (Team 5)" />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}