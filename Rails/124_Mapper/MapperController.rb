class MapperController < ApplicationController
  before_action :set_mapper, only: [:show, :edit, :update, :destroy]

  # GET /mapper
  def index
    @mappers = Mapper.all
    render json: @mappers
  end

  # GET /mapper/1
  def show
    render json: @mapper
  end

  # POST /mapper
  def create
    @mapper = Mapper.new(mapper_params)

    if @mapper.save
      render json: @mapper, status: :created
    else
      render json: @mapper.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /mapper/1
  def update
    if @mapper.update(mapper_params)
      render json: @mapper
    else
      render json: @mapper.errors, status: :unprocessable_entity
    end
  end

  # DELETE /mapper/1
  def destroy
    @mapper.destroy
    head :no_content
  end

  private

  def set_mapper
    @mapper = Mapper.find(params[:id])
  end

  def mapper_params
    params.require(:mapper).permit(:name)
  end
end
