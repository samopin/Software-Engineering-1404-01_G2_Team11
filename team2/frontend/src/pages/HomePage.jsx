import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Search, FileText, ArrowLeft } from 'lucide-react'
import { api } from '../api'

export default function HomePage() {
  const [searchQuery, setSearchQuery] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleSearch = async (e) => {
    e.preventDefault()
    if (!searchQuery.trim()) return

    setLoading(true)
    setError('')
    try {
      await api.getArticle(searchQuery.trim())
      navigate(`/articles/${encodeURIComponent(searchQuery.trim())}`)
    } catch (err) {
      if (err.status === 404) {
        setError('Article not found.')
      } else {
        setError('An error occurred. Make sure you are logged in.')
      }
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-[calc(100vh-4rem)] flex flex-col">
      <section className="flex-1 flex flex-col items-center justify-center px-4 py-20">
        <div className="text-center max-w-2xl mx-auto">
          <div className="mb-6">
            <div className="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-indigo-500/10 mb-6">
              <FileText className="w-10 h-10 text-indigo-400" />
            </div>
          </div>

          <h1 className="text-4xl sm:text-5xl font-bold text-white mb-4 leading-tight">
            Wiki Service
          </h1>
          <p className="text-gray-400 text-lg mb-10">
            Search for an article by name to view, edit, or vote on it.
          </p>

          <form onSubmit={handleSearch} className="w-full max-w-lg mx-auto">
            <div className="relative">
              <Search className="absolute right-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500" />
              <input
                type="text"
                placeholder="Enter article name..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full bg-gray-800 border border-gray-700 rounded-xl py-3.5 pr-12 pl-4 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent text-right"
                dir="ltr"
              />
            </div>
            {error && (
              <p className="mt-3 text-red-400 text-sm">{error}</p>
            )}
            <button
              type="submit"
              disabled={loading}
              className="mt-4 w-full bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-3 rounded-xl transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'Searching...' : 'Search Article'}
            </button>
          </form>
        </div>
      </section>

      <footer className="border-t border-gray-800 py-6 text-center">
        <a
          href="/"
          className="inline-flex items-center gap-2 text-gray-500 hover:text-gray-300 transition-colors text-sm"
        >
          <ArrowLeft className="w-4 h-4" />
          Back to Main Dashboard
        </a>
      </footer>
    </div>
  )
}
