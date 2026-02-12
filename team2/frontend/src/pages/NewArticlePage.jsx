import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { PlusCircle, Loader2 } from 'lucide-react'
import { api } from '../api'

export default function NewArticlePage() {
  const [name, setName] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!name.trim()) return

    setLoading(true)
    setError('')
    try {
      const data = await api.createArticle(name.trim())
      navigate(`/articles/${encodeURIComponent(data.name)}`)
    } catch (err) {
      setError(err.data?.detail || 'Failed to create article. Make sure you are logged in.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-lg mx-auto px-4 py-16">
      <div className="bg-gray-800 rounded-2xl border border-gray-700 p-8">
        <div className="flex items-center gap-3 mb-6">
          <div className="p-2 bg-indigo-500/10 rounded-lg">
            <PlusCircle className="w-6 h-6 text-indigo-400" />
          </div>
          <h1 className="text-xl font-bold text-white">Create New Article</h1>
        </div>

        <form onSubmit={handleSubmit}>
          <label className="block text-sm font-medium text-gray-400 mb-2">
            Article Name
          </label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="e.g. my-first-article"
            className="w-full bg-gray-900 border border-gray-700 rounded-xl py-3 px-4 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
            dir="ltr"
          />

          {error && (
            <p className="mt-3 text-red-400 text-sm">{error}</p>
          )}

          <button
            type="submit"
            disabled={loading}
            className="mt-6 w-full bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-3 rounded-xl transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            {loading ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                Creating...
              </>
            ) : (
              'Create Article'
            )}
          </button>
        </form>
      </div>
    </div>
  )
}
