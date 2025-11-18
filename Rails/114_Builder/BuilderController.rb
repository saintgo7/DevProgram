class BuilderController < ApplicationController
  before_action :set_builder, only: [:show, :edit, :update, :destroy]

  # GET /builder
  def index
    @builders = Builder.all
    render json: @builders
  end

  # GET /builder/1
  def show
    render json: @builder
  end

  # POST /builder
  def create
    @builder = Builder.new(builder_params)

    if @builder.save
      render json: @builder, status: :created
    else
      render json: @builder.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /builder/1
  def update
    if @builder.update(builder_params)
      render json: @builder
    else
      render json: @builder.errors, status: :unprocessable_entity
    end
  end

  # DELETE /builder/1
  def destroy
    @builder.destroy
    head :no_content
  end

  private

  def set_builder
    @builder = Builder.find(params[:id])
  end

  def builder_params
    params.require(:builder).permit(:name)
  end
end
