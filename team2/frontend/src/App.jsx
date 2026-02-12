import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import HomePage from './pages/HomePage'
import ArticlePage from './pages/ArticlePage'
import NewArticlePage from './pages/NewArticlePage'

export default function App() {
  return (
    <div className="min-h-screen bg-light text-dark">
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/articles/new" element={<NewArticlePage />} />
        <Route path="/articles/:name" element={<ArticlePage />} />
      </Routes>
    </div>
  )
}
