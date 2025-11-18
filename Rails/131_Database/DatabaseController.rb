class DatabaseController < ApplicationController
  before_action :set_database, only: [:show, :edit, :update, :destroy]

  # GET /database
  def index
    @databases = Database.all
    render json: @databases
  end

  # GET /database/1
  def show
    render json: @database
  end

  # POST /database
  def create
    @database = Database.new(database_params)

    if @database.save
      render json: @database, status: :created
    else
      render json: @database.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /database/1
  def update
    if @database.update(database_params)
      render json: @database
    else
      render json: @database.errors, status: :unprocessable_entity
    end
  end

  # DELETE /database/1
  def destroy
    @database.destroy
    head :no_content
  end

  private

  def set_database
    @database = Database.find(params[:id])
  end

  def database_params
    params.require(:database).permit(:name)
  end
end
