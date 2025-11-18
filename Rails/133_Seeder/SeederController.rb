class SeederController < ApplicationController
  before_action :set_seeder, only: [:show, :edit, :update, :destroy]

  # GET /seeder
  def index
    @seeders = Seeder.all
    render json: @seeders
  end

  # GET /seeder/1
  def show
    render json: @seeder
  end

  # POST /seeder
  def create
    @seeder = Seeder.new(seeder_params)

    if @seeder.save
      render json: @seeder, status: :created
    else
      render json: @seeder.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /seeder/1
  def update
    if @seeder.update(seeder_params)
      render json: @seeder
    else
      render json: @seeder.errors, status: :unprocessable_entity
    end
  end

  # DELETE /seeder/1
  def destroy
    @seeder.destroy
    head :no_content
  end

  private

  def set_seeder
    @seeder = Seeder.find(params[:id])
  end

  def seeder_params
    params.require(:seeder).permit(:name)
  end
end
