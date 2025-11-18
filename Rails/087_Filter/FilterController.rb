class FilterController < ApplicationController
  before_action :set_filter, only: [:show, :edit, :update, :destroy]

  # GET /filter
  def index
    @filters = Filter.all
    render json: @filters
  end

  # GET /filter/1
  def show
    render json: @filter
  end

  # POST /filter
  def create
    @filter = Filter.new(filter_params)

    if @filter.save
      render json: @filter, status: :created
    else
      render json: @filter.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /filter/1
  def update
    if @filter.update(filter_params)
      render json: @filter
    else
      render json: @filter.errors, status: :unprocessable_entity
    end
  end

  # DELETE /filter/1
  def destroy
    @filter.destroy
    head :no_content
  end

  private

  def set_filter
    @filter = Filter.find(params[:id])
  end

  def filter_params
    params.require(:filter).permit(:name)
  end
end
