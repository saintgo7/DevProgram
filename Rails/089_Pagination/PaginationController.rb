class PaginationController < ApplicationController
  before_action :set_pagination, only: [:show, :edit, :update, :destroy]

  # GET /pagination
  def index
    @paginations = Pagination.all
    render json: @paginations
  end

  # GET /pagination/1
  def show
    render json: @pagination
  end

  # POST /pagination
  def create
    @pagination = Pagination.new(pagination_params)

    if @pagination.save
      render json: @pagination, status: :created
    else
      render json: @pagination.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /pagination/1
  def update
    if @pagination.update(pagination_params)
      render json: @pagination
    else
      render json: @pagination.errors, status: :unprocessable_entity
    end
  end

  # DELETE /pagination/1
  def destroy
    @pagination.destroy
    head :no_content
  end

  private

  def set_pagination
    @pagination = Pagination.find(params[:id])
  end

  def pagination_params
    params.require(:pagination).permit(:name)
  end
end
