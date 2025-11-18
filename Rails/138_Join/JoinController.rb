class JoinController < ApplicationController
  before_action :set_join, only: [:show, :edit, :update, :destroy]

  # GET /join
  def index
    @joins = Join.all
    render json: @joins
  end

  # GET /join/1
  def show
    render json: @join
  end

  # POST /join
  def create
    @join = Join.new(join_params)

    if @join.save
      render json: @join, status: :created
    else
      render json: @join.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /join/1
  def update
    if @join.update(join_params)
      render json: @join
    else
      render json: @join.errors, status: :unprocessable_entity
    end
  end

  # DELETE /join/1
  def destroy
    @join.destroy
    head :no_content
  end

  private

  def set_join
    @join = Join.find(params[:id])
  end

  def join_params
    params.require(:join).permit(:name)
  end
end
