class CacheController < ApplicationController
  before_action :set_cache, only: [:show, :edit, :update, :destroy]

  # GET /cache
  def index
    @caches = Cache.all
    render json: @caches
  end

  # GET /cache/1
  def show
    render json: @cache
  end

  # POST /cache
  def create
    @cache = Cache.new(cache_params)

    if @cache.save
      render json: @cache, status: :created
    else
      render json: @cache.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /cache/1
  def update
    if @cache.update(cache_params)
      render json: @cache
    else
      render json: @cache.errors, status: :unprocessable_entity
    end
  end

  # DELETE /cache/1
  def destroy
    @cache.destroy
    head :no_content
  end

  private

  def set_cache
    @cache = Cache.find(params[:id])
  end

  def cache_params
    params.require(:cache).permit(:name)
  end
end
