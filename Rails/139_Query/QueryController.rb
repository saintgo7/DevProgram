class QueryController < ApplicationController
  before_action :set_query, only: [:show, :edit, :update, :destroy]

  # GET /query
  def index
    @querys = Query.all
    render json: @querys
  end

  # GET /query/1
  def show
    render json: @query
  end

  # POST /query
  def create
    @query = Query.new(query_params)

    if @query.save
      render json: @query, status: :created
    else
      render json: @query.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /query/1
  def update
    if @query.update(query_params)
      render json: @query
    else
      render json: @query.errors, status: :unprocessable_entity
    end
  end

  # DELETE /query/1
  def destroy
    @query.destroy
    head :no_content
  end

  private

  def set_query
    @query = Query.find(params[:id])
  end

  def query_params
    params.require(:query).permit(:name)
  end
end
