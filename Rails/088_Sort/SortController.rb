class SortController < ApplicationController
  before_action :set_sort, only: [:show, :edit, :update, :destroy]

  # GET /sort
  def index
    @sorts = Sort.all
    render json: @sorts
  end

  # GET /sort/1
  def show
    render json: @sort
  end

  # POST /sort
  def create
    @sort = Sort.new(sort_params)

    if @sort.save
      render json: @sort, status: :created
    else
      render json: @sort.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /sort/1
  def update
    if @sort.update(sort_params)
      render json: @sort
    else
      render json: @sort.errors, status: :unprocessable_entity
    end
  end

  # DELETE /sort/1
  def destroy
    @sort.destroy
    head :no_content
  end

  private

  def set_sort
    @sort = Sort.find(params[:id])
  end

  def sort_params
    params.require(:sort).permit(:name)
  end
end
