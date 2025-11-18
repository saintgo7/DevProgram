class SearchController < ApplicationController
  before_action :set_search, only: [:show, :edit, :update, :destroy]

  # GET /search
  def index
    @searchs = Search.all
    render json: @searchs
  end

  # GET /search/1
  def show
    render json: @search
  end

  # POST /search
  def create
    @search = Search.new(search_params)

    if @search.save
      render json: @search, status: :created
    else
      render json: @search.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /search/1
  def update
    if @search.update(search_params)
      render json: @search
    else
      render json: @search.errors, status: :unprocessable_entity
    end
  end

  # DELETE /search/1
  def destroy
    @search.destroy
    head :no_content
  end

  private

  def set_search
    @search = Search.find(params[:id])
  end

  def search_params
    params.require(:search).permit(:name)
  end
end
